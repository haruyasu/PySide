from PySide.QtGui import *
from PySide.QtCore import *
import sys

class MainDialog(QDialog):
    # new
    # myOwnSignal = Signal(str)
    myOwnSignal = Signal((int,), (str,))

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)

        self.btn1 = QPushButton("Button!")
        layout = QVBoxLayout()
        layout.addWidget(self.btn1)
        self.setLayout(layout)

        # old
        # self.connect(self.btn1, SIGNAL("clicked()"), self.btn1clicked)
        # self.connect(self, SIGNAL("myOwnSignal()"), self.myOwnSignalEmitted)

        # new
        self.btn1.clicked.connect(self.btn1clicked)
        self.myOwnSignal.connect(self.myOwnSignalEmitted)
        self.myOwnSignal[str].connect(self.myOwnSignalEmitted)

    def btn1clicked(self):
        # old
        # self.emit(SIGNAL("myOwnSignal()"))

        # new
        # self.myOwnSignal.emit("Whatever.")
        # self.myOwnSignal.emit(10)
        self.myOwnSignal[str].emit("Hello")

    def myOwnSignalEmitted(self, param):
        # print "SIGNAL EMITTED! " + param
        print "SIGNAL EMITTED! " + str(param)
        print type(param)

app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()
