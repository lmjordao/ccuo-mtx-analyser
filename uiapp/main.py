import sys
from uiapp.mainapp.mainwind import Ui_MainWindow
from PyQt5 import QtWidgets

if __name__ == '__main__':

    print("Start")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
