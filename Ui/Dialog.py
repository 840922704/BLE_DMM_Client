# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\xy790\Desktop\Sub_Research\IoT_Sensor\BLE\V0.3\Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(407, 448)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_start = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_2.addWidget(self.pushButton_start)
        self.pushButton_stop = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.horizontalLayout_2.addWidget(self.pushButton_stop)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_LCD = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(72)
        self.label_LCD.setFont(font)
        self.label_LCD.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_LCD.setAutoFillBackground(False)
        self.label_LCD.setText("")
        self.label_LCD.setTextFormat(QtCore.Qt.AutoText)
        self.label_LCD.setScaledContents(True)
        self.label_LCD.setAlignment(QtCore.Qt.AlignCenter)
        self.label_LCD.setObjectName("label_LCD")
        self.verticalLayout_2.addWidget(self.label_LCD)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_function = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_function.setFont(font)
        self.label_function.setText("")
        self.label_function.setObjectName("label_function")
        self.horizontalLayout_5.addWidget(self.label_function)
        self.label_unit = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_unit.setFont(font)
        self.label_unit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_unit.setObjectName("label_unit")
        self.horizontalLayout_5.addWidget(self.label_unit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.Label_Current_points = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Label_Current_points.setFont(font)
        self.Label_Current_points.setText("")
        self.Label_Current_points.setObjectName("Label_Current_points")
        self.horizontalLayout_4.addWidget(self.Label_Current_points)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.Label_max_points = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Label_max_points.setFont(font)
        self.Label_max_points.setText("")
        self.Label_max_points.setObjectName("Label_max_points")
        self.horizontalLayout_4.addWidget(self.Label_max_points)
        self.SliderBar_buffered_points = QtWidgets.QSlider(Dialog)
        self.SliderBar_buffered_points.setOrientation(QtCore.Qt.Horizontal)
        self.SliderBar_buffered_points.setObjectName("SliderBar_buffered_points")
        self.horizontalLayout_4.addWidget(self.SliderBar_buffered_points)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.graph_layout = QtWidgets.QVBoxLayout()
        self.graph_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.graph_layout.setContentsMargins(-1, 0, -1, 0)
        self.graph_layout.setSpacing(0)
        self.graph_layout.setObjectName("graph_layout")
        self.verticalLayout.addLayout(self.graph_layout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.pushButton_datapath = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton_datapath.setFont(font)
        self.pushButton_datapath.setObjectName("pushButton_datapath")
        self.horizontalLayout.addWidget(self.pushButton_datapath)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>Address:</p></body></html>"))
        self.pushButton_start.setText(_translate("Dialog", "Start"))
        self.pushButton_stop.setText(_translate("Dialog", "Stop"))
        self.label_unit.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "Max buffer of graph:"))
        self.label_2.setText(_translate("Dialog", "/"))
        self.checkBox.setText(_translate("Dialog", "Save Data"))
        self.pushButton_datapath.setText(_translate("Dialog", "Data Path"))
        self.label_3.setText(_translate("Dialog", "     Record Speed:"))
        self.comboBox.setItemText(0, _translate("Dialog", "High"))
        self.comboBox.setItemText(1, _translate("Dialog", "Medium"))
        self.comboBox.setItemText(2, _translate("Dialog", "Low"))
