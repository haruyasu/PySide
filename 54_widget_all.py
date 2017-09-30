import os, sys
from functools import partial
import time
from PySide import QtCore, QtGui

LOGO_IMAGE = os.path.dirname(__file__) + "/img/ben.png"

print LOGO_IMAGE

class GUI(QtGui.QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Widget ALL")
        # self.resize(600, 400)
        wrapper = QtGui.QWidget()
        self.setCentralWidget(wrapper)
        mainLayout = QtGui.QVBoxLayout()
        wrapper.setLayout(mainLayout)

        # --- first row ---
        firstHolizontalArea = QtGui.QHBoxLayout()
        firstHolizontalArea.setSpacing(20)
        mainLayout.addLayout(firstHolizontalArea)

        labelArea = QtGui.QVBoxLayout()
        firstHolizontalArea.addLayout(labelArea)

        labelWidget = QtGui.QLabel("Text is shown like this.")
        labelArea.addWidget(labelWidget)

        imageWidget = QtGui.QLabel()
        imageWidget.setPixmap(QtGui.QPixmap(LOGO_IMAGE))
        labelArea.addWidget(imageWidget)
        labelArea.addStretch()

        textArea = QtGui.QTextEdit()
        textArea.setPlainText("Text are \ncan be set\nmultiple lines and HTML")
        firstHolizontalArea.addWidget(textArea)

        mainLayout.addWidget(self.makeHorizontalLine())

        # --- second row ---


    def makeHorizontalLine(self):
        hline = QtGui.QFrame()
        hline.setFrameShape(QtGui.QFrame.HLine)
        hline.setFrameShadow(QtGui.QFrame.Sunken)
        return hline

def main():
    app = QtGui.QApplication(sys.argv)
    ui = GUI()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()