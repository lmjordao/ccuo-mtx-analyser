# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treeView.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from uiapp.settingsapp.settingswind import *

class Ui_TreeWindow(object):
    def setupUi(self, MainWindow, id):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 388)
        MainWindow.setWindowIcon(QIcon('gallery/csw.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(20, 20, 391, 281))
        self.treeView.setObjectName("treeView")
        self.populate()
        self.lineEdit_path = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_path.setGeometry(QtCore.QRect(20, 320, 301, 25))
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.pushButton_select = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_select.setGeometry(QtCore.QRect(330, 320, 75, 27))
        self.pushButton_select.setObjectName("pushButton_select")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        global xid
        xid = id

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Open File"))
        self.pushButton_select.setText(_translate("MainWindow", "Select"))
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.context_menu)
        self.treeView.clicked.connect(self.get_text)
        self.pushButton_select.clicked.connect(self.button_click)


    def get_text(self, text):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        print(file_path)
        self.lineEdit_path.setText(file_path)

    def button_click(self):
        self.lineEdit_path.text()
        print("SELECT BTN")


        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_SettingsWindow()
        self.ui.populateLabels(self.Window, self.lineEdit_path.text())


    def populate(self):
        path = ""
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath((QtCore.QDir.rootPath()))
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(path))
        self.treeView.setSortingEnabled(True)

    def context_menu(self):
        menu = QtWidgets.QMenu()
        open = menu.addAction("Open one explorer")
        open.triggered.connect(self.open_file)

        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

    def open_file(self):
        # id = [1-7]
        # 1-pushButton_open_local_componets
        # 2-pushButton_open_lotrain_ccuoprojectname
        # 3-pushButton_open_lotrain_project
        # 4-pushButton_open_lotrain_genericpad
        # 5-pushButton_open_ea_ccuoprojectname
        # 6-pushButton_open_ea_project
        # 7-pushButton_open_ea_genericpad

        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        print(file_path)
        os.startfile(file_path)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_TreeWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
