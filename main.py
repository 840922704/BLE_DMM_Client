import os
import sys
from datetime import datetime
import locale
import logging
import time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog
from PyQt5.QtCore import pyqtSignal, QTranslator
from PyQt5.QtGui import QFont, QIcon
import pyqtgraph as pg
from qt_material import QtStyleTools

from Ui.MainWindow import Ui_MainWindow
from Ui.Dialog import Ui_Dialog
from decoder import type_detecter, decoder_1, decoder_2, decoder_3, decoder_4

import asyncio
from bleak import BleakClient
import threading
from bleak import BleakScanner

#ADDRESS = ""

class DialogWindow(QDialog, Ui_Dialog):
    newdata = pyqtSignal(object) # 创建信号
    # stop_thread = pyqtSignal()
    def __init__(self, parent=None):
        super(DialogWindow, self).__init__(parent)
        self.setupUi(self)
        #self.setWindowTitle('BLE DMM Monitor')
        self.retranslateUi(self)
        # QTranslator
        self.trans = QTranslator()
        pass

        #BLE Devices
        self.logger = logging.getLogger(__name__)
        self.t = []
        self.digi = []
        self.char = []
        self.label_LCD.setText("0.000")

        self.pushButton_start.clicked.connect(self.startThread)
        self.pushButton_stop.clicked.connect(self.stopThread)
        self.pushButton_datapath.clicked.connect(self.data_path)

        # Set SliderBar_buffered_points
        self.SliderBar_buffered_points.setMinimum(1)
        self.SliderBar_buffered_points.setMaximum(300)
        self.SliderBar_buffered_points.setValue(100)
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
                    print('Start get data')
                    self.stop_collect = 0
                    type = type_detecter.type(bytes(await client.read_gatt_char(8, use_cached=1)).hex())
                    while self.stop_collect == 0 : 
                        
                        value = bytes(await client.read_gatt_char(8, use_cached=1)).hex()
                        #print(type(value))
                        #print(value)
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

                        #self.t.append(time.time())
                        now = datetime.now()
                        self.t = now.strftime('%Y-%m-%d %H:%M:%S.%f')
                        #self.t = now.strftime('%Y-%m-%d %H:%M:%S')
                        #self.t = time.asctime(time.localtime(time.time()))
                        
                        self.B_function = ' '.join(B[0])
                        self.B_unit = ' '.join(B[1])
                        print(A)
                        print(self.B_function+" "+self.B_unit)
                        self.digi = str(A)
                        self.char_function = str(self.B_function)
                        self.char_unit = str(self.B_unit)
                        signal = (self.t,(self.digi, self.char_unit),self.char_function)
                        self.newdata.emit(signal)
                        print(self.t)
                        #self.lcdNumber.display(signal[1][0])
                        #self.label_unit.setText(signal[1][1])
                        #self.newdata.emit(signal)
                        time.sleep(1/3)
                    # when stop button be pushed, clear connection

                    self.label_LCD.setText("0.000")

                    #self.plot_plt.clear()
                    self.data_list =[]
                    self.datestamp = []
                    self.b = 0
                    try:
                        f.close()
                    except:
                        print("No file opened")
                    print("Closed successfully")
                except:
                    print('Connection Closed')
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
            print(self.ADDRESS_dialog)
            print("No device found")
            self.pushButton_start.setEnabled(True)

    #Data save directory
    def data_path(self):
        self.Filepath = QtWidgets.QFileDialog.getExistingDirectory(None,"Please Choose File Path",self.Filepath)  # 起始路径
        if not os.path.exists(self.Filepath):
            os.makedirs(self.Filepath)

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
            now = datetime.now()
            if self.checkBox_isChecked != self.checkBox.isChecked():
                if self.checkBox.isChecked() == True:
                    if not os.path.exists(self.Filepath):
                        os.makedirs(self.Filepath)
                    f = open(self.Filepath +'\\' + now.strftime('%Y-%m-%d')+'.txt',mode = 'a', encoding='utf-8')
                    f.write(str(signal[0])[:-5]+"   "+signal[1][0]+" "+signal[1][1]+" "+signal[2]+"\n")
                elif self.checkBox.isChecked() == False:
                    f.close()
            else:
                if self.checkBox.isChecked() == True:
                    f.write(str(signal[0])[:-5]+"   "+signal[1][0]+" "+signal[1][1]+" "+signal[2]+"\n")
                #elif self.checkBox.isChecked() == False:
                    #f.close()



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, QtStyleTools):
    search_complete = pyqtSignal(object) # create signal
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
            }
            self.apply_stylesheet(self, theme='dark_lightgreen.xml', invert_secondary=False, extra=extra)

        def Theme_Light(self):
            extra = {
                # Font
                'font_family': 'Microsoft YaHei',
                'font_size': '12px',
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

            self.trans.load("./Ui/MainWindow_en.qm")
            _app.installTranslator(self.trans) # Re-translate the main interface
            self.retranslateUi(self)

            self.trans.load("./Ui/Dialog_en.qm")
            _app.installTranslator(self.dialog.trans) # Install translations for submodules
            self.dialog.retranslateUi(self.dialog) # translation submodule

            pass

        def _trigger_zh_cn(self):
            print("[MainWindow] Change to zh_CN")
            
            _app = QtWidgets.QApplication.instance()

            self.trans.load("./Ui/MainWindow_zh_CN.qm")
            _app.installTranslator(self.trans)
            self.retranslateUi(self)

            self.trans.load("./Ui/Dialog_zh_CN.qm")
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
        "<p style=\" margin-top:6px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">BLE_DMM_Client v3.0</span></p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Release page: </span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/840922704/BLE_DMM_Client\"><span style=\" font-size:12pt; text-decoration: underline; color:#99cc33;\">https://github.com/840922704/BLE_DMM_Client</span></a></p>\n")
    
    # Dialog Window
    def open_dialog(self):
        
        # Send ADDRESS to DialogWindow
        DialogWindow.ADDRESS_dialog = self.ADDRESS
        self.dialog.show()
        self.dialog.label.setText("Address: "+self.ADDRESS)

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('Logo.png'))
    f = QFont("Microsoft YaHei",12)
    app.setFont(f)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())