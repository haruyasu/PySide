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

        border = 'border-width: 4px; border-color: orange;'
        buttonHoverStyle = 'QPushButton:hover{%s}' % (border)
        style += buttonHoverStyle

        ui.setStyleSheet(style)

        def clickEvent(button):
            self.ui.textField.setText(button.text())
            style = 'QLineEdit[text="Red"]{background-color: red; color: white}'
            style += 'QLineEdit[text="Blue"]{background-color: blue; color: white}'
            style += 'QLineEdit[text="Yellow"]{background-color: yellow; color: black}'
            self.ui.textField.setStyleSheet(style)

        ui.redButton.clicked.connect(fnt.partial(clickEvent, ui.redButton))
        ui.blueButton.clicked.connect(fnt.partial(clickEvent, ui.blueButton))
        ui.yellowButton.clicked.connect(fnt.partial(clickEvent, ui.yellowButton))

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()