import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)

wid = QtGui.QWidget()
wid.resize(300,200)
wid.setWindowTitle("Simple Example")
wid.show()

sys.exit(app.exec_())
