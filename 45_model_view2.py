import sys
from PySide import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Molde View')
        self.model = QtGui.QStandardItemModel()
        listView = QtGui.QListView()
        treeView = QtGui.QTreeView()
        tableView = QtGui.QTableView()
        listView.setModel(self.model)
        treeView.setModel(self.model)
        tableView.setModel(self.model)
        listView.setSelectionModel(tableView.selectionModel())
        treeView.setSelectionModel(tableView.selectionModel())
        self.setItems()

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(listView)
        vbox.addWidget(treeView)
        vbox.addWidget(tableView)

        self.setLayout(vbox)
        self.resize(450, 450)

    def setItems(self):
        for row in range(3):
            for column in range(4):
                item = QtGui.QStandardItem('%d, %d' % (row, column))
                self.model.setItem(row, column, item)
                for i in range(2):
                    for j in range(3):
                        child = QtGui.QStandardItem('%d, %d' % (i, j))
                        item.setChild(i, j, child)

def main():
    app = QtGui.QApplication(sys.argv)
    ui = Example()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
