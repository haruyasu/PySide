import sys
from PySide import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QtGui.QLabel("Linux", self)
        self.lbl.move(50, 150)

        combo = QtGui.QComboBox(self)
        combo.addItem("Linux")
        combo.addItem("Windows")
        combo.addItem("Mac")
        combo.move(50, 50)
        combo.activated[str].connect(self.onActivated)

        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle('Combo Box')
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()