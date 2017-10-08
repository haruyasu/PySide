from PySide.QtGui import *
from PySide.QtCore import *
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/ui')

import mainGui

class MainWindow(QMainWindow, mainGui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # old syntax
        # self.connect(self.actionExit, SIGNAL("triggered()"), self.exitApp)

        # new syntax
        self.actionExit.triggered.connect(self.exitApp)

    def exitApp(self):
        sys.exit(0)

app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()
