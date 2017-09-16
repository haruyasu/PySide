import sys
from PySide import QtGui, QtCore

DATA = [{'name': 'Model', 'color': [255, 0, 0]},
        {'name': 'View', 'color': [0, 255, 0]},
        {'name': 'Delegate', 'color': [0, 0, 255]}]

class CustomListDelegate(QtGui.QStyledItemDelegate):
    def __init__(self, parent=None):
        super(CustomListDelegate, self).__init__(parent)

    def paint(self, painter, option, index):
        if option.state & QtGui.QStyle.State_Selected:
            bgBrush = QtGui.QBrush(QtGui.QColor(60, 60, 60))
            bgPen = QtGui.QPen(QtGui.QColor(60, 60, 60), 0.5, QtCore.Qt.SolidLine)
            painter.setPen(bgPen)
            painter.setBrush(bgBrush)
            painter.drawRect(option.rect)

        name = index.data(QtCore.Qt.DisplayRole)
        color = index.data(QtCore.Qt.ForegroundRole)
        pen = QtGui.QPen(QtGui.QColor(color), 0.5, QtCore.Qt.SolidLine)
        painter.setPen(pen)
        painter.drawText(option.rect, QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft, 'Name: ' + name)

    def sizeHint(self, option, index):
        return QtCore.QSize(100, 80)

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
        listDelegate = CustomListDelegate()
        listView.setItemDelegate(listDelegate)

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
