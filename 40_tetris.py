import sys
from PySide import QtGui, QtCore

class Tetris(QtGui.QMainWindow):
    def __init__(self):
        super(Tetris, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle('Tetris')

def main():
    app = QtGui.QApplication(sys.argv)
    t = Tetris()
    t.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()