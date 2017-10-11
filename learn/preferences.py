from PySide.QtCore import *
from PySide.QtGui import *


class Preferences(QDialog):

    checkboxsig = Signal(bool) #for PyQt4 it's pyqtSignal(bool)

    def __init__(self, parent=None, showToolbar=True):
        super(Preferences, self).__init__(parent)

        self.resize(200, 100)
        self.setWindowTitle("Preferences")

        self.checkBox = QCheckBox("show main toolbar")
        self.checkBox.setChecked(showToolbar)
        closeBtn = QPushButton("close")

        layout = QVBoxLayout()
        layout.addWidget(self.checkBox)
        layout.addWidget(closeBtn)

        self.setLayout(layout)

        closeBtn.clicked.connect(self.close)
        self.checkBox.stateChanged.connect(self.checkBoxStateChanged)


    def checkBoxStateChanged(self):
        self.checkboxsig.emit(self.checkBox.isChecked())

