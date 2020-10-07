# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from configparser import ConfigParser

from PyQt5.QtWidgets import QButtonGroup

from uiapp.treeviewapp.treeviewapp import Ui_TreeWindow

configPath = "C:/Users/USER-Admin/Desktop/Gloob/config.ini"


class Ui_SettingsWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 468)
        MainWindow.setWindowIcon(QIcon('gallery/csw.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_configfile = QtWidgets.QLabel(self.centralwidget)
        self.label_configfile.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label_configfile.setObjectName("label_configfile")
        self.label_local = QtWidgets.QLabel(self.centralwidget)
        self.label_local.setGeometry(QtCore.QRect(20, 50, 55, 16))
        self.label_local.setObjectName("label_local")
        self.label_local_componets = QtWidgets.QLabel(self.centralwidget)
        self.label_local_componets.setGeometry(QtCore.QRect(40, 70, 81, 16))
        self.label_local_componets.setObjectName("label_local_componets")
        self.label_lotrain = QtWidgets.QLabel(self.centralwidget)
        self.label_lotrain.setGeometry(QtCore.QRect(20, 110, 55, 16))
        self.label_lotrain.setObjectName("label_lotrain")
        self.label_lotrain_ccuoprojectname = QtWidgets.QLabel(self.centralwidget)
        self.label_lotrain_ccuoprojectname.setGeometry(QtCore.QRect(40, 130, 121, 16))
        self.label_lotrain_ccuoprojectname.setObjectName("label_lotrain_ccuoprojectname")
        self.label_lotrain_project = QtWidgets.QLabel(self.centralwidget)
        self.label_lotrain_project.setGeometry(QtCore.QRect(40, 160, 55, 16))
        self.label_lotrain_project.setObjectName("label_lotrain_project")
        self.label_lotrain_genericpad = QtWidgets.QLabel(self.centralwidget)
        self.label_lotrain_genericpad.setGeometry(QtCore.QRect(40, 190, 91, 16))
        self.label_lotrain_genericpad.setObjectName("label_lotrain_genericpad")
        self.label_ea = QtWidgets.QLabel(self.centralwidget)
        self.label_ea.setGeometry(QtCore.QRect(20, 230, 55, 16))
        self.label_ea.setObjectName("label_ea")
        self.label_ea_ccuoprojectname = QtWidgets.QLabel(self.centralwidget)
        self.label_ea_ccuoprojectname.setGeometry(QtCore.QRect(40, 250, 121, 16))
        self.label_ea_ccuoprojectname.setObjectName("label_ea_ccuoprojectname")
        self.label_ea_project = QtWidgets.QLabel(self.centralwidget)
        self.label_ea_project.setGeometry(QtCore.QRect(40, 280, 55, 16))
        self.label_ea_project.setObjectName("label_ea_project")
        self.label_ea_genericpad = QtWidgets.QLabel(self.centralwidget)
        self.label_ea_genericpad.setGeometry(QtCore.QRect(40, 310, 91, 16))
        self.label_ea_genericpad.setObjectName("label_ea_genericpad")
        self.lineEdit_componets = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_componets.setGeometry(QtCore.QRect(110, 70, 281, 22))
        self.lineEdit_componets.setObjectName("lineEdit_componets")
        self.lineEdit_lotrain_ccuoprojectname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_lotrain_ccuoprojectname.setGeometry(QtCore.QRect(160, 130, 231, 22))
        self.lineEdit_lotrain_ccuoprojectname.setObjectName("lineEdit_lotrain_ccuoprojectname")
        self.lineEdit_lotrain_project = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_lotrain_project.setGeometry(QtCore.QRect(90, 160, 301, 22))
        self.lineEdit_lotrain_project.setObjectName("lineEdit_lotrain_project")
        self.lineEdit_lotrain_genericpad = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_lotrain_genericpad.setGeometry(QtCore.QRect(120, 190, 271, 22))
        self.lineEdit_lotrain_genericpad.setObjectName("lineEdit_lotrain_genericpad")
        self.lineEdit_ea_ccuoprojectname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ea_ccuoprojectname.setGeometry(QtCore.QRect(160, 250, 231, 22))
        self.lineEdit_ea_ccuoprojectname.setObjectName("lineEdit_ea_ccuoprojectname")
        self.lineEdit_ea_project = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ea_project.setGeometry(QtCore.QRect(90, 280, 301, 22))
        self.lineEdit_ea_project.setObjectName("lineEdit_ea_project")
        self.lineEdit_ea_genericpad = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ea_genericpad.setGeometry(QtCore.QRect(120, 310, 271, 22))
        self.lineEdit_ea_genericpad.setObjectName("lineEdit_ea_genericpad")
        self.pushButton_open_local_componets = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_local_componets.setGeometry(QtCore.QRect(400, 70, 41, 24))
        self.pushButton_open_local_componets.setObjectName("pushButton_open_local_componets")
        self.pushButton_open_lotrain_ccuoprojectname = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_lotrain_ccuoprojectname.setGeometry(QtCore.QRect(400, 130, 41, 24))
        self.pushButton_open_lotrain_ccuoprojectname.setObjectName("pushButton_open_lotrain_ccuoprojectname")
        self.pushButton_open_lotrain_project = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_lotrain_project.setGeometry(QtCore.QRect(400, 160, 41, 24))
        self.pushButton_open_lotrain_project.setObjectName("pushButton_open_lotrain_project")
        self.pushButton_open_lotrain_genericpad = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_lotrain_genericpad.setGeometry(QtCore.QRect(400, 190, 41, 24))
        self.pushButton_open_lotrain_genericpad.setObjectName("pushButton_open_lotrain_genericpad")
        self.pushButton_open_ea_ccuoprojectname = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_ea_ccuoprojectname.setGeometry(QtCore.QRect(400, 250, 41, 24))
        self.pushButton_open_ea_ccuoprojectname.setObjectName("pushButton_open_ea_ccuoprojectname")
        self.pushButton_open_ea_project = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_ea_project.setGeometry(QtCore.QRect(400, 280, 41, 24))
        self.pushButton_open_ea_project.setObjectName("pushButton_open_ea_project")
        self.pushButton_open_ea_genericpad = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_ea_genericpad.setGeometry(QtCore.QRect(400, 310, 41, 24))
        self.pushButton_open_ea_genericpad.setObjectName("pushButton_open_ea_genericpad")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(310, 390, 61, 24))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(380, 390, 61, 24))
        self.pushButton_close.setObjectName("pushButton_close")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 476, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Settigns"))
        self.label_configfile.setText(_translate("MainWindow", "Config file"))
        self.label_local.setText(_translate("MainWindow", "Local:"))
        self.label_local_componets.setText(_translate("MainWindow", "Componets:"))
        self.label_lotrain.setText(_translate("MainWindow", "LOTRAIN:"))
        self.label_lotrain_ccuoprojectname.setText(_translate("MainWindow", "ccuo_project_name:"))
        self.label_lotrain_project.setText(_translate("MainWindow", "project:"))
        self.label_lotrain_genericpad.setText(_translate("MainWindow", "generic_pad:"))
        self.label_ea.setText(_translate("MainWindow", "EA:"))
        self.label_ea_ccuoprojectname.setText(_translate("MainWindow", "ccuo_project_name:"))
        self.label_ea_project.setText(_translate("MainWindow", "project:"))
        self.label_ea_genericpad.setText(_translate("MainWindow", "generic_pad:"))

        #-----------------------------btn-----------------------------------------
        self.pushButton_open_local_componets.setText(_translate("MainWindow", "Open"))
        #self.pushButton_open_local_componets.clicked.connect(self.opentree)

        self.pushButton_open_lotrain_ccuoprojectname.setText(_translate("MainWindow", "Open"))
        #self.pushButton_open_lotrain_ccuoprojectname.clicked.connect(self.opentree)

        self.pushButton_open_lotrain_project.setText(_translate("MainWindow", "Open"))
        #self.pushButton_open_lotrain_project.clicked.connect(self.opentree)

        self.pushButton_open_lotrain_genericpad.setText(_translate("MainWindow", "Open"))
        #self.pushButton_open_lotrain_genericpad.clicked.connect(self.opentree)

        self.pushButton_open_ea_ccuoprojectname.setText(_translate("MainWindow", "Open"))
        #self.pushButton_open_ea_ccuoprojectname.clicked.connect(self.opentree)

        self.pushButton_open_ea_project.setText(_translate("MainWindow", "Open"))
        #self.pushButton_open_ea_project.clicked.connect(self.opentree)

        self.pushButton_open_ea_genericpad.setText(_translate("MainWindow", "Open"))
        #self.pushButton_open_ea_genericpad.clicked.connect(self.opentree)


        self.btn_grp = QButtonGroup()
        self.btn_grp.setExclusive(True)
        self.btn_grp.addButton(self.pushButton_open_local_componets, 1)
        self.btn_grp.addButton(self.pushButton_open_lotrain_ccuoprojectname, 2)
        self.btn_grp.addButton(self.pushButton_open_lotrain_project, 3)
        self.btn_grp.addButton(self.pushButton_open_lotrain_genericpad, 4)
        self.btn_grp.addButton(self.pushButton_open_ea_ccuoprojectname, 5)
        self.btn_grp.addButton(self.pushButton_open_ea_project, 6)
        self.btn_grp.addButton(self.pushButton_open_ea_genericpad, 7)

        self.btn_grp.buttonClicked[int].connect(self.opentree)
        # -----------------------------btn-----------------------------------------

        ##############################
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.pushButton_save.clicked.connect(self.button_click)
        self.pushButton_close.setText(_translate("MainWindow", "close"))
        self.pushButton_close.clicked.connect(QCoreApplication.instance().quit)


        ##############################
        configPath = "C:/Users/USER-Admin/Desktop/Gloob/configback.ini"
        config = ConfigParser()
        config.read(configPath)
        ##############################

        self.lineEdit_componets.setText(_translate("MainWindow", config["local"]["components"]))
        self.lineEdit_componets.setStyleSheet("color: grey")
        #self.lineEdit_componets.textChanged.connect(self.sync_lineEdit)

        ##############################

        self.lineEdit_lotrain_ccuoprojectname.setText(_translate("MainWindow", config["lotrain"]["ccuo_project_name"]))
        self.lineEdit_lotrain_ccuoprojectname.setStyleSheet("color: grey")

        self.lineEdit_lotrain_project.setText(_translate("MainWindow", config["lotrain"]["project"]))
        self.lineEdit_lotrain_project.setStyleSheet("color: grey")

        self.lineEdit_lotrain_genericpad.setText(_translate("MainWindow", config["lotrain"]["generic_pad"]))
        self.lineEdit_lotrain_genericpad.setStyleSheet("color: grey")

        ##############################

        self.lineEdit_ea_ccuoprojectname.setText(_translate("MainWindow", config["ea"]["ccuo_project_name"]))
        self.lineEdit_ea_ccuoprojectname.setStyleSheet("color: grey")

        self.lineEdit_ea_project.setText(_translate("MainWindow", config["ea"]["project"]))
        self.lineEdit_ea_project.setStyleSheet("color: grey")

        self.lineEdit_ea_genericpad.setText(_translate("MainWindow", config["ea"]["generic_pad"]))
        self.lineEdit_ea_genericpad.setStyleSheet("color: grey")
        ##############################

    def sync_lineEdit(self, text):
        print(text)

    def button_click(self):
        # shost is a QString object
        componets_save = self.lineEdit_componets.text()

        lotrain_ccuoprojectname_save = self.lineEdit_lotrain_ccuoprojectname.text()
        lotrain_project_save = self.lineEdit_lotrain_project.text()
        lotrain_genericpad_save = self.lineEdit_lotrain_genericpad.text()

        ea_ccuoprojectname_save = self.lineEdit_ea_ccuoprojectname.text()
        ea_project_save = self.lineEdit_ea_project.text()
        ea_genericpad_save = self.lineEdit_ea_genericpad.text()
        saveonConfigfile(componets_save, lotrain_ccuoprojectname_save, lotrain_project_save, lotrain_genericpad_save, ea_ccuoprojectname_save, ea_project_save, ea_genericpad_save)

        print(componets_save)
        print(lotrain_ccuoprojectname_save)
        print(lotrain_project_save)
        print(lotrain_genericpad_save)
        print(ea_ccuoprojectname_save)
        print(ea_project_save)
        print(ea_genericpad_save)

    def opentree(self, id):
        # id = [1-7]
        # 1-pushButton_open_local_componets
        # 2-pushButton_open_lotrain_ccuoprojectname
        # 3-pushButton_open_lotrain_project
        # 4-pushButton_open_lotrain_genericpad
        # 5-pushButton_open_ea_ccuoprojectname
        # 6-pushButton_open_ea_project
        # 7-pushButton_open_ea_genericpad

        for btn in self.btn_grp.buttons():
            if btn is self.btn_grp.button(id):
                print(id)

        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_TreeWindow()
        self.ui.setupUi(self.Window,id)
        self.Window.show()


    def populateLabels(self, text):

        if id == 1:
            # 1-local_componets
            self.lineEdit_lotrain_ccuoprojectname.setText(text)
        if id == 2:
            # 2-lotrain_ccuoprojectname
            self.lineEdit_lotrain_ccuoprojectname.setText(text)
        if id == 3:
            # 3-lotrain_project
            self.lineEdit_lotrain_ccuoprojectname.setText(text)
        if id == 4:
            # 4-lotrain_genericpad
            self.lineEdit_lotrain_ccuoprojectname.setText(text)
        if id == 5:
            # 5-ea_ccuoprojectname
            self.lineEdit_lotrain_ccuoprojectname.setText(text)
        if id == 6:
            # 6-ea_project
            self.lineEdit_lotrain_ccuoprojectname.setText(text)
        if id == 7:
            # 7-ea_genericpad
            self.lineEdit_lotrain_ccuoprojectname.setText(text)


def saveonConfigfile(componets_save, lotrain_ccuoprojectname_save, lotrain_project_save, lotrain_genericpad_save, ea_ccuoprojectname_save, ea_project_save, ea_genericpad_save):

    configPath = "C:/Users/USER-Admin/Desktop/Gloob/config.ini"
    config = ConfigParser()
    config.read(configPath)

    config.set("local", "components", componets_save)

    config.set("lotrain", "ccuo_project_name", lotrain_ccuoprojectname_save)
    config.set("lotrain", "project", lotrain_project_save)
    config.set("lotrain", "generic_pad", lotrain_genericpad_save)

    config.set("ea", "ccuo_project_name", ea_ccuoprojectname_save)
    config.set("ea", "project", ea_project_save)
    config.set("ea", "generic_pad", ea_genericpad_save)

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SettingsWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
