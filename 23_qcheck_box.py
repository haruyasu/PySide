import sys
from PySide import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        cb = QtGui.QCheckBox('Show Title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle('Check Box')
        self.show()

    def changeTitle(self, state):
        if state == QtCore.Qt.Checked:
            self.setWindowTitle('Check ON')
        else:
            self.setWindowTitle('Check OFF')

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()