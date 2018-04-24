from PyQt5 import QtWidgets
from future.moves import sys

from au10.networker import Networker
from au10.window import Ui_MainWindow


class Controller(QtWidgets.QMainWindow):
    """
    Controlles the GUI
    """


    def __init__(self):
        super(Controller, self).__init__()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

        self.__ui.hostInp.setText("127.0.0.1")
        self.__ui.portInp.setText("8099")
        self.__ui.outTxt.setReadOnly(True)
        self.bind_buttons()

    def bind_buttons(self):
        """
        Binds the buttons to functions.
        :return: None
        """
        self.__ui.checkBtn.clicked.connect(self.handle_check)
        self.__ui.closeBtn.clicked.connect(self.handle_close)
        self.__ui.resetBtn.clicked.connect(self.handle_reset)

    def handle_check(self):
        """
        Handles the check: that is sending a blocking request and resolving possible errors.
        When the request is successful the output textBox will show the formatted info.
        :return: None
        """
        try:

            self.__ui.outTxt.setText("Language: <b>{0}</b><br />Probability: <b>{1}%</b> <br /> reliable? <b>{2}</b> <br /> Language ISO: <b>{3}</b>".format(
                *Networker.make_request(self.__ui.hostInp.text(),
                                        self.__ui.portInp.text(),
                                        self.__ui.inpText.toPlainText())
            ))
        except Exception as e:
            se = str(e)
            print("Exception occoured")
            self.__ui.outTxt.setText("<b>An error occoured:</b> <br />{}".format(se))

    def handle_close(self):
        """
        Called when the user presses the close button
        :return:
        """
        sys.exit(0)

    def handle_reset(self):
        """
        called when the user presses the reset button.
        Clears all Inputs
        :return: None
        """
        self.__ui.inpText.setText("")
        self.__ui.outTxt.setText("")
