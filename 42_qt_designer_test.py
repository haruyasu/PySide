import os, sys
from PySide import QtCore, QtGui
from PySide.QtUiTools import QUiLoader
import functools as fnt

uiFile = 'ui/test.ui'

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        loader = QUiLoader()
        self.ui = loader.load(uiFile)
        self.setCentralWidget(self.ui)
        self.setWindowTitle('Qt Designer Test')
        self.resize(350, 120)

        ui = self.ui
        ui.redButton.setStyleSheet('QPushButton{ background-color: red; color: white; }')
        ui.blueButton.setStyleSheet('QPushButton{ background-color: blue; color: white; }')
        ui.yellowButton.setStyleSheet('QPushButton{ background-color: yellow; color: black; }')

        h = 30
        style = ''
        height = 'height: %spx;' % (h)
        border = 'border-style: solid; border-width: 2px; border-color: gray;'
        borderRadius = 'border-radius: %spx;' % (h / 2)
        buttonStyle = 'QPushButton{%s %s %s}' % (height, border, borderRadius)
        style += buttonStyle
        ui.setStyleSheet(style)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()