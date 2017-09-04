import sys
from PySide import QtCore, QtGui

def main():
    app = QtGui.QApplication(sys.argv)

    myListModel1 = QtGui.QStringListModel(["Lion", "Monkey", "Tiger", "Cat"])

    myListView1 = QtGui.QListView()
    myListView2 = QtGui.QListView()

    myListView1.setModel(myListModel1)
    myListView2.setModel(myListModel1)

    myListView1.show()
    myListView2.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()