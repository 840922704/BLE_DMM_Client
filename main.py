import os
import sys
from datetime import datetime
import locale
import logging
import time

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox, QDialog, QSplashScreen
from PySide6.QtCore import Signal, QTranslator
from PySide6.QtGui import QFont, QIcon, QPixmap
import pyqtgraph as pg

from Ui.MainWindow import Ui_MainWindow
from Ui.Dialog import Ui_Dialog
import Ui.resources_rc
from decoder import type_detecter, decoder_1, decoder_2, decoder_3, decoder_4

from qt_material import QtStyleTools

import asyncio
from bleak import BleakClient
import threading
from bleak import BleakScanner

# pyinstaller splash screen
import importlib
if '_PYIBoot_SPLASH' in os.environ and importlib.util.find_spec("pyi_splash"):
    import pyi_splash
    pyi_splash.update_text('UI Loaded ...')
    pyi_splash.close()
    # log.info('Splash screen closed.')

ADDRESS_Signal = ""

class DialogWindow(QDialog, Ui_Dialog):
    newdata = Signal(object) # 创建信号
    # stop_thread = Signal()

    def __init__(self, parent=None):
        super(DialogWindow, self).__init__(parent)
        self.setupUi(self)
        #self.setWindowTitle('BLE DMM Monitor')
        self.retranslateUi(self)
        # QTranslator
        self.trans = QTranslator()
        pass

        # Get global ADDRESS_Signal
        global ADDRESS_Signal
        self.ADDRESS_dialog = ADDRESS_Signal
        self.label.setText("Address: "+ADDRESS_Signal)

        #BLE Devices
        self.logger = logging.getLogger(__name__)
        self.top_collect = 1
        self.label_LCD.setText("0.000")

        self.pushButton_start.clicked.connect(self.startThread)
        self.pushButton_stop.clicked.connect(self.stopThread)
        self.pushButton_datapath.clicked.connect(self.data_path)

        # Set SliderBar_buffered_points
        self.SliderBar_buffered_points.setMinimum(1)
        self.SliderBar_buffered_points.setMaximum(1000)
        self.SliderBar_buffered_points.setValue(300)
        self.Label_max_points.setText(str(self.SliderBar_buffered_points.value()*100).zfill(5))
        self.SliderBar_buffered_points.valueChanged.connect(self.SliderBar_value)

        self.Filepath = os.path.abspath('.')+"\\"+"Saved_Data"
        if not os.path.exists(self.Filepath):
            os.makedirs(self.Filepath)
        self.pushButton_datapath.setToolTip(self.Filepath)

        # Add pyqtgraph to qtwidget
        # Set x aixs to datestamp
        self.datestamp = []
        
        self.plot_plt = pg.PlotWidget(axisItems={'bottom': pg.DateAxisItem()})
        # Remove export item because pyqtgraph will crash when compiled by nuitka.
        # (issues #1532 in nuitka, Github)
        # self.plot_plt.scene().contextMenu = None
        self.plot_plt.setMinimumHeight(200)
        self.plot_plt.showGrid(x=True,y=True)
        self.graph_layout.addWidget(self.plot_plt)
        
        # plot speed

        #self.comboBox.currentIndexChanged.connect(self.selectionchange)
        self.comboBox.setCurrentIndex(1) 
        self.comboBox_currentIndex = 1
        self.checkBox_isChecked = self.checkBox.isChecked()
        self.a = 0
        self.plotspeed_param = 11

        #plot clear (buffer points)
        self.b = 0
        self.plotclear_param = 10000
        self.Label_Current_points.setText(str(self.b).zfill(5))
        self.newdata.connect(self.plot)

        self.data_list = []

        # stopThread
        self.stop_collect = 0

    def SliderBar_value(self):
        value=self.SliderBar_buffered_points.value()*100 # get sliderbar value
        self.Label_max_points.setText(str(value).zfill(5))
        
        self.plotclear_param = value

    def stopThread(self):
        self.stop_collect = 1
        self.pushButton_start.setEnabled(True)
        print ('Stop the thread...')
        
    def closeEvent(self, event):
        self.stopThread()
        pass

    # getdata
    def startThread(self):
        '''
        这里使用python的threading.Thread构造线程，并将线程设置为守护线程，这样
        主线程退出后守护线程也会跟着销毁
        Here we use python's threading.Thread to construct a thread, and set the thread as a daemon thread, 
        so that the daemon thread will also be destroyed after the main thread exits.
        '''
        print('Daemon thread starts')
        self.pushButton_start.setEnabled(False)
        print('Start listening to Bluetooth')
        thread = threading.Thread(target=self.getdata)
        thread.setDaemon(True) # 守护线程

        thread.start() # 启动线程
    # mian loop to get data
    async def data(self,ADDRESS_dialog):
        try:
            async with BleakClient(ADDRESS_dialog) as client:
                self.logger.info(f"Connected: {client.is_connected}")
                try:

                    t = []
                    digi = []
                    char = []
                    char_unit = []
                    char_function = []

                    print('Start get data')
                    self.stop_collect = 0
                    try:
                        type = ''
                        type = type_detecter.type(bytes(await client.read_gatt_char(8, use_cached=1)).hex())
                        print(type)
                        if type == None:
                            self.stop_collect = 1
                    except Exception as e:
                        print (e)
                        print("Fail to type_detecter.type")
                    #print(self.stop_collect)
                    while self.stop_collect == 0 : 
                        print("Enter Main Loop")
                        try :
                            #value = "1b8470b1592ad97a66fa3a"
                            value = bytes(await client.read_gatt_char(8, use_cached=1)).hex()
                            #print(type(value))
                            print(value)
                        except Exception as e:
                            print (e)
                        if type == '1':
                            A = decoder_1.printdigit(decoder_1.decode(value))
                            B = decoder_1.printchar(decoder_1.decode(value))
                        elif type == '2':
                            A = decoder_2.printdigit(decoder_2.decode(value))
                            B = decoder_2.printchar(decoder_2.decode(value))
                        elif type == '3':
                            A = decoder_3.printdigit(decoder_3.decode(value))
                            B = decoder_3.printchar(decoder_3.decode(value))
                        elif type == '4':
                            A = decoder_4.printdigit(decoder_4.decode(value))
                            B = decoder_4.printchar(decoder_4.decode(value))
                        else :
                            self.stop_collect = 1
                        print("Get decode")
                        #t.append(time.time())
                        now = datetime.now()
                        t = now.strftime('%Y-%m-%d %H:%M:%S.%f')
                        #t = now.strftime('%Y-%m-%d %H:%M:%S')
                        #t = time.asctime(time.localtime(time.time()))
                        
                        print("Get Time")

                        try:
                            B_function = ' '.join(B[0])
                            B_unit = ' '.join(B[1])
                            print(A)
                            print(B_function+" "+B_unit)
                            digi = str(A)
                            char_function = str(B_function)
                            char_unit = str(B_unit)

                            signal = (t,(digi,char_unit),char_function)
                            print(signal)
                            self.newdata.emit(signal)
                        except Exception as e:
                            print (e)
                            
                        print(t)
                        #self.lcdNumber.display(signal[1][0])
                        #self.label_unit.setText(signal[1][1])
                        #self.newdata.emit(signal)
                        time.sleep(1/3)
                        
                        print("Finish One Loop")
                    # when stop button be pushed, clear connection

                    self.label_LCD.setText("0.000")

                    #self.plot_plt.clear()
                    self.data_list =[]
                    self.datestamp = []
                    self.b = 0
                    try:
                        f.close()
                        print("Closed successfully")
                    except:
                        print("No file opened")
                        self.label_LCD.setText("0.000")
                        self.pushButton_start.setEnabled(True)
                except:
                    #print('Connection Closed')
                    self.label_LCD.setText("0.000")
                    self.pushButton_start.setEnabled(True)
        except:
            self.pushButton.start.setEnabled(True)
            print('Failed to asyn '+ADDRESS_dialog)
    

    def getdata(self):
        try:
            print(self.ADDRESS_dialog)
            asyncio.run(self.data(sys.argv[1] if len(sys.argv) == 2 else self.ADDRESS_dialog))
        except:
            #print(self.ADDRESS_dialog)
            print("No device found")
            self.pushButton_start.setEnabled(True)

    #Data save directory
    def data_path(self):
        now = datetime.now()
        File_MAC = ''.join(char for char in self.ADDRESS_dialog if char.isalnum())
        Default_Filepath = self.Filepath
        Choose_Filepath = QtWidgets.QFileDialog.getSaveFileName(self, 'Save Path', str(self.Filepath +'\\' + File_MAC + "_" + now.strftime('%Y-%m-%d')+'.txt'), "txt(*.txt)';;*(*.*)")
        self.Filepath = Choose_Filepath[0]
        if self.Filepath == "":
            self.Filepath = Default_Filepath
            return 0
        print(self.Filepath)
        self.pushButton_datapath.setToolTip(self.Filepath)
        f = open(self.Filepath, mode='a', encoding='utf-8')
        f.close()

        #self.Filepath = QtWidgets.QFileDialog.getExistingDirectory(None,"Please Choose File Path",self.Filepath)  # 起始路径

    # real time plot
    def plot(self,signal):
        #self.plot_plt.clear()
        # combobox for different speed
        self.comboBox_currentIndex = self.comboBox.currentIndex()
        if self.comboBox_currentIndex == 1:
            self.plotspeed_param = 5
        elif self.comboBox_currentIndex == 0:
            self.plotspeed_param = 0
        elif self.comboBox_currentIndex == 2:
            self.plotspeed_param = 23

        # real time lcd and label
        self.label_LCD.setText(str(signal[1][0]))

        self.label_unit.setText(signal[1][1])
        self.label_function.setText(signal[2])
        # pyqtgraph with different speed
        if self.a > self.plotspeed_param:
            try:
                plot_data = float(signal[1][0])
            except:
                plot_data = float(0)
            self.data_list.append(plot_data)
            self.datestamp.append(datetime(
            int(str(signal[0])[0:4]),
            int(str(signal[0])[5:7]),
            int(str(signal[0])[8:10]),
            int(str(signal[0])[11:13]),
            int(str(signal[0])[14:16]),
            int(str(signal[0])[17:19]),
            int(str(signal[0])[20:26])))
            # Prevent data accumulat
            self.plot_plt.clear()
            #self.plot_plt.plot().setData(self.data_list,pen='w')
            self.plot_plt.plot(x=[x.timestamp() for x in self.datestamp],y=self.data_list,pen='w')
            self.a = 0
            self.b = self.b + 1
        self.a = self.a + 1
        # Clear the pyqtgraph screen regularly
        self.Label_Current_points.setText(str(self.b).zfill(5))
        if self.b > self.plotclear_param:
            self.plot_plt.clear()
            self.data_list=[]
            self.b = 0
            self.datestamp = []
        # write to file, with speed control and checkbox control
        if self.a > self.plotspeed_param:
            if self.checkBox_isChecked != self.checkBox.isChecked():
                if self.checkBox.isChecked() == True:
                    #if not os.path.exists(self.Filepath):
                        #os.system(r"touch {}".format(self.Filepath))
                    f = open(self.Filepath, mode='a', encoding='utf-8')
                    f.write(str(signal[0])[:-5]+"   "+signal[1][0]+" "+signal[1][1]+" "+signal[2]+"\n")
                elif self.checkBox.isChecked() == False:
                    f.close()
            else:
                if self.checkBox.isChecked() == True:
                    f.write(str(signal[0])[:-5]+"   "+signal[1][0]+" "+signal[1][1]+" "+signal[2]+"\n")
                #elif self.checkBox.isChecked() == False:
                    #f.close()



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, QtStyleTools):
    search_complete = Signal(object) # create signal
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        #self.setWindowTitle('BLE DMM Client')


        ## Themes
        def Theme_Dark(self):
            extra = {
                # Font
                'font_family': 'Microsoft YaHei',
                'font_size': '12px',
                # environ
                'pyside6': True,
            }
            self.apply_stylesheet(self, theme='dark_lightgreen.xml', extra=extra)
            tooltip_stylesheet = """
                QToolTip {
                    background-color: black;
                }
                QComboBox {
                    color: white;
                }
            """
            self.setStyleSheet(self.styleSheet()+tooltip_stylesheet)
        def Theme_Light(self):
            extra = {
                # Font
                'font_family': 'Microsoft YaHei',
                'font_size': '12px',
                # environ
                'pyside6': True,
            }
            self.apply_stylesheet(self, theme='light_cyan_500.xml', invert_secondary=True, extra=extra)
        def Theme_Native(self):
            self.apply_stylesheet(self, theme='default', invert_secondary=True)
        #The default theme is dark
        Theme_Dark(self)
        self.actionNative.triggered.connect(lambda:Theme_Native(self))
        self.actionDark.triggered.connect(lambda:Theme_Dark(self))
        self.actionLight.triggered.connect(lambda:Theme_Light(self))


        #  QTranslator
        self.trans = QTranslator()

        # Connect to the slot function
        self.actionEnglish.triggered.connect(lambda:_trigger_english(self))
        self.actionChinese.triggered.connect(lambda:_trigger_zh_cn(self))
        self.dialog = DialogWindow(self)

        def _trigger_english(self):
            print("[MainWindow] Change to English")
            self.trans.load("")
            _app = QtWidgets.QApplication.instance()  # Get app instance

            self.trans.load(":/MainWindow_en.qm")
            _app.installTranslator(self.trans) # Re-translate the main interface
            self.retranslateUi(self)

            self.trans.load(":/Dialog_en.qm")
            _app.installTranslator(self.dialog.trans) # Install translations for submodules
            self.dialog.retranslateUi(self.dialog) # translation submodule

            pass

        def _trigger_zh_cn(self):
            print("[MainWindow] Change to zh_CN")
            
            _app = QtWidgets.QApplication.instance()

            self.trans.load(":/MainWindow_zh_CN.qm")
            _app.installTranslator(self.trans)
            self.retranslateUi(self)

            self.trans.load(":/Dialog_zh_CN.qm")
            _app.installTranslator(self.dialog.trans)
            self.dialog.retranslateUi(self.dialog)
        
        # Auto detect language
        def system_language_detect(self):
            if locale.getdefaultlocale()[0]=="zh_CN":
                _trigger_zh_cn(self)
            else:
                _trigger_english(self)
        system_language_detect(self)

        #self.setWindowIcon(QIcon('Logo.png'))
        self.count = 0


        # BLE Devices Below
        self.logger = logging.getLogger(__name__)

        self.devices = []
        self.pushButton_search.clicked.connect(self.startThread_devices)
        self.progressBar.setValue(0)
        self.search_complete.connect(self.searching)
        #self.pushButton_search.clicked.connect(self.searching)
        self.listWidget.itemClicked.connect(self.change_address)

        self.pushButton.clicked.connect(self.open_dialog)

        self.ADDRESS = ""


    # About page
        self.actionAbout.triggered.connect(self.open_about)
    def open_about(self):
        QMessageBox.about(self,'About',
        "<p style=\" margin-top:6px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">BLE_DMM_Client v3.2</span></p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Release page: </span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/840922704/BLE_DMM_Client/releases\"><span style=\" font-size:12pt; text-decoration: underline; color:#99cc33;\">https://github.com/840922704/BLE_DMM_Client</span></a></p>\n")
    
    # Dialog Window
    def open_dialog(self):
        
        # Send ADDRESS to DialogWindow
        global ADDRESS_Signal
        ADDRESS_Signal = self.ADDRESS
        if self.ADDRESS == "":
            print("self.ADDRESS is None!")
        else:
            DialogWindow(self).show()

## BLE Devices Below

    def startThread_devices(self):
        '''
        daemon thread
        '''
        print('Searching Bluetooth devices')
        thread = threading.Thread(target=self.search_devices_2)
        thread.setDaemon(True) # 守护线程
        thread.start() # 启动线程
    def search_devices_2(self):
        asyncio.run(self.search_devices())
        
    async def search_devices(self):
        signal = 0
        self.search_complete.emit(signal)
        self.devices = []
        devices = await BleakScanner.discover()
        self.listWidget.clear()

        for d in devices:
            self.listWidget.addItem(str(d))
            print(d)
        signal = 100
        self.search_complete.emit(signal)
    # progressbar flash
    def searching (self,signal):
        if signal == 0:
            self.progressBar.setRange(0,0)
        if signal == 100:
            self.progressBar.setRange(0,100)
            self.progressBar.setValue(100)
        #for a in range(1,101,1):
        #    self.progressBar.setValue(a)
        #    time.sleep(0.05)
    def change_address(self, item):
        self.ADDRESS = item.text().split(": ")[0]
        print(self.ADDRESS)

def main():
    app = QtWidgets.QApplication(sys.argv)
    # pyside6 splash screen
    #splash = QSplashScreen()
    #splash.setPixmap(QPixmap(":/splash.png"))
    #splash.show()
    app.setWindowIcon(QIcon(':/Logo.ico'))
    f = QFont("Microsoft YaHei",12)
    app.setFont(f)
    mainWindow = MainWindow()
    mainWindow.show()
    # close splash screen
    #splash.finish(mainWindow)
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()