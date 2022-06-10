from pkgutil import get_data
import sys
from tkinter import dialog
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
import logging
import asyncio
from Ui.MainWindow import Ui_MainWindow
from Ui.Dialog import Ui_Dialog
from decoder import decoder_11, decoder_10
from bleak import BleakClient
import time
import threading
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtGui import QFont
from bleak import BleakScanner


ADDRESS = ""

class DialogWindow(QDialog, Ui_Dialog):
    newdata = pyqtSignal(object) # 创建信号
    stop_thread = pyqtSignal()  # 定义关闭子线程的信号
    def __init__(self, parent=None):
        super(DialogWindow, self).__init__(parent)
        self.setupUi(self)
        #BLE Devices
        self.logger = logging.getLogger(__name__)
        self.t = []
        self.digi = []
        self.char = []
        self.lcdNumber.setStyleSheet("line-height:200%")
        self.lcdNumber.setDigitCount(8)
        self.pushButton.clicked.connect(self.startThread)
        self.newdata.connect(self.data)

        

#    def update_progressbar(self, p_int):
#        self.progressBar.setValue(p_int)

    def closeEvent(self, event):
        self.stop_thread.emit()
        print("X is cliked")
        pass

#getdata
#    def startThread(self):
    def startThread(self):
        '''
        这里使用python的threading.Thread构造线程，并将线程设置为守护线程，这样
        主线程退出后守护线程也会跟着销毁
        Here we use python's threading.Thread to construct a thread, and set the thread as a daemon thread, 
        so that the daemon thread will also be destroyed after the main thread exits.
        '''
        print('Daemon thread starts')
        self.pushButton.setEnabled(False)
        print('Start listening to Bluetooth')
        thread = threading.Thread(target=self.getdata)
        thread.setDaemon(True) # 守护线程

        thread.start() # 启动线程
        
    async def data(self, ADDRESS):
        try:
            async with BleakClient(ADDRESS) as client:
                self.logger.info(f"Connected: {client.is_connected}")
                try:
                    print('now')
                    while 1: 
                        value = bytes(await client.read_gatt_char(8, use_cached=1))
                        ## print(value.hex())
                        ## 11 Byte DMM
                        if len(value.hex()) == 22:
                            A = decoder_11.printdigit(decoder_11.decode(value.hex()))
                            B = decoder_11.printchar(decoder_11.decode(value.hex()))
                        ## 10 Byte DMM
                        elif len(value.hex()) == 20:
                            A = decoder_10.printdigit(decoder_10.decode(value.hex()))
                            B = decoder_10.printchar(decoder_10.decode(value.hex()))

                        #self.t.append(time.time())
                        self.t = time.asctime(time.localtime(time.time()))
                        print(A)
                        self.digi = round(float(A), 3)
                        self.char = str(B)
                        signal = (self.t,(self.digi, self.char))
                        self.newdata.emit(signal)
                        print(self.t)
                        self.lcdNumber.display(signal[1][0])
                        self.label_2.setText(signal[1][1])
                        time.sleep(1/3)

                except:
                    print('Connection Closed')
                    self.pushButton.setEnabled(True)
        except:
            self.pushButton.setEnabled(True)
            print('Failed to asyn'+ADDRESS)
    

    def getdata(self):
        try:
            print(ADDRESS)
            asyncio.run(self.data(sys.argv[1] if len(sys.argv) == 2 else ADDRESS))
        except:
            print(ADDRESS)
            print("No device found")






class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.count = 0

###BLE Devices Below
        self.logger = logging.getLogger(__name__)


        self.devices = []
        self.pushButton_search.clicked.connect(self.startThread_devices)
        self.progressBar.setValue(0)
        self.pushButton_search.clicked.connect(self.searching)
        self.listWidget.itemClicked.connect(self.change_address)

        self.pushButton.clicked.connect(self.open_dialog)



###BLE Devices Above


    def open_dialog(self):
        dialog = DialogWindow(self)
        dialog.show()
        dialog.label.setText("MAC:"+ADDRESS)

#        self.thread = RunThread(self.count)
#        self.count += 1
#        self.thread.update_pb.connect(dialog.update_progressbar)
#        self.thread.update_pb.connect(dialog.startThread)

#        self.thread.start()

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
        self.devices = []
        devices = await BleakScanner.discover()
        self.listWidget.clear()
        for d in devices:
            self.listWidget.addItem(str(d))
            print(d)

    def searching (self):
        self.progressBar.setValue(100)
    def change_address(self, item):
        global ADDRESS
        ADDRESS = item.text().split(": ")[0]
        print(ADDRESS)
###BLE Devices Above


#class RunThread(QThread):
#    update_pb = pyqtSignal(int)
#
#    def __init__(self, count):
#        super().__init__()
#        self.count = count
#
#    def run(self):
#        for i in range(1, 101):
#            print('thread_%s' % self.count, i, QThread().currentThreadId())
#            self.update_pb.emit(i)
#            time.sleep(1)
#        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
