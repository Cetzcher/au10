"""
Entrypoint for the program
creates a QApplication and hosts the GUI.
"""
from PyQt5 import QtWidgets
import sys
from au10.Controller import Controller

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show()
    sys.exit(app.exec_())