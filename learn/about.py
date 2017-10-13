from PySide.QtCore import *
from PySide.QtGui import *

class About(QDialog):
    def __init__(self, parent=None):
        super(About, self).__init__(parent)

        self.resize(200, 150)
        self.setWindowTitle("About")

        label1 = QLabel('About Me', self)
        label1.move(70, 20)

        closeBtn = QPushButton("close")

        layout = QVBoxLayout()
        layout.addWidget(closeBtn)

        self.setLayout(layout)

        closeBtn.clicked.connect(self.close)