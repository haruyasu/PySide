from PySide.QtGui import *
from PySide.QtCore import *
import sys

class ZeroSpinBox(QSpinBox):
    zeros = 0
    atZero = Signal(int, int)

    def __init__(self, parent=None):
        super(ZeroSpinBox, self).__init__(parent)

        self.valueChanged.connect(self.check_zero)

    def check_zero(self, value):
        if value == 0:
            self.zeros += 1
            self.constant = 5
            self.atZero.emit(self.zeros, self.constant)


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.dial = QDial()
        self.dial.setNotchesVisible(True)

        self.spinbox = ZeroSpinBox()

        layout = QVBoxLayout()
        layout.addWidget(self.dial)
        layout.addWidget(self.spinbox)
        self.setLayout(layout)

        self.dial.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.dial.setValue)

        self.spinbox.atZero.connect(self.print_value)

    def print_value(self, zeros, constant):
        print "The SpinBox has been at zero {0} times".format(zeros)
        print "The constant is {0}".format(constant)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
