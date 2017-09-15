import sys
from PySide import QtGui, QtCore

DATA = [{'name': 'Model', 'color': [255, 0, 0]},
        {'name': 'View', 'color': [0, 0, 255]},
        {'name': 'Delegate', 'color': [0, 255, 0]}]

class CustomListModel(QtCore.QAbstractListModel):
    def __init__(self, parent=None, data=[]):
        super(CustomListModel, self).__init__(parent)
        self.items = data

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.items)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid() or not 0 <= index.row() < len(self.items):
            return None

        if role == QtCore.Qt.DisplayRole:
            return self.items[index.row()].get('name')
        elif role == QtCore.Qt.ForegroundRole:
            color = self.items[index.row()].get('color', [])
            return QtGui.QColor(*color)

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if not index.isValid() or not 0 <= index.row() < len(self.items) or not value:
            return False

        if role == QtCore.Qt.EditRole:
            self.items[index.row()]['name'] = value.toString()
            self.dataChanged.emit(index, index)
            return True
        else:
            return False

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        listModel = CustomListModel(data=DATA)
        listView = QtGui.QListView()
        listView.setModel(listModel)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(listView)
        self.setLayout(vbox)

        self.setWindowTitle('Delegate Example')
        self.resize(500, 500)

def main():
    app = QtGui.QApplication(sys.argv)
    ui = Example()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()