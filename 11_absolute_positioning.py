import sys
from PySide import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        label1 = QtGui.QLabel('Zetcode', self)
        label1.move(15, 20)

        label2 = QtGui.QLabel('Tutorial', self)
        label2.move(30, 40)

        label3 = QtGui.QLabel('PySide', self)
        label3.move(60, 80)

        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle('Absolute')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()