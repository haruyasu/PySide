import sys
from PySide import QtGui, QtCore

DATA = [{'name': 'Model', 'color': [255, 0, 0], 'id': 0, 'priority': 1},
        {'name': 'View', 'color': [0, 255, 0], 'id': 1, 'priority': 2},
        {'name': 'Delegate', 'color': [0, 0, 255], 'id': 2, 'priority': 3}]

ID_ROLE = QtCore.Qt.UserRole
AGE_ROLE = QtCore.Qt.UserRole + 1

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

        color = index.data(QtCore.Qt.ForegroundRole)
        pen = QtGui.QPen(QtGui.QColor(color), 0.5, QtCore.Qt.SolidLine)
        painter.setPen(pen)

        if index.column() == 0:
            name = index.data(QtCore.Qt.DisplayRole)
            painter.drawText(option.rect, QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter, str(name))
        elif index.column() == 1:
            id = index.data(ID_ROLE)
            painter.drawText(option.rect, QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter, str(id))
        elif index.column() == 2:
            priority = index.data(AGE_ROLE)
            painter.drawText(option.rect, QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter, str(priority))

    def sizeHint(self, option, index):
        return QtCore.QSize(0, 40)

    def createEditor(self, parent, option, index):
        editor = QtGui.QLineEdit(parent)
        return editor

    def setEditorData(self, editor, index):
        value = ''
        if index.column() == 0:
            value = index.model().data(index, QtCore.Qt.DisplayRole)
        elif index.column() == 1:
            value = index.model().data(index, ID_ROLE)
        elif index.column() == 2:
            value = index.model().data(index, AGE_ROLE)
        editor.setText(str(value))

    def setModelData(self, editor, model, index):
        value = editor.text()
        if index.column() == 0:
            model.setData(index, value, QtCore.Qt.DisplayRole)
        elif index.column() == 1:
            model.setData(index, value, ID_ROLE)
        elif index.column() == 2:
            model.setData(index, value, AGE_ROLE)

class CustomListModel(QtGui.QStandardItemModel):
    def __init__(self, parent=None, data=[]):
        super(CustomListModel, self).__init__(parent)
        self.items = data
        self.refreshItems()

    def refreshItems(self):
        idx = 0
        for item in self.items:
            for key, value in item.items():
                if key == 'name':
                    name_item = QtGui.QStandardItem(value)
                    self.setItem(idx, 0, name_item)
                elif key == 'id':
                    id_item = QtGui.QStandardItem(value)
                    self.setItem(idx, 1, id_item)
                elif key == 'priority':
                    age_item = QtGui.QStandardItem(value)
                    self.setItem(idx, 2, age_item)
            idx += 1

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
        elif role == ID_ROLE:
            return self.items[index.row()].get('id')
        elif role == AGE_ROLE:
            return self.items[index.row()].get('priority')
        else:
            return None

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if not index.isValid() or not 0 <= index.row() < len(self.items):
            return False

        if not value:
            return False

        if role == QtCore.Qt.DisplayRole:
            self.items[index.row()]['name'] = str(value)
            self.dataChanged.emit(index, index)
            return True
        elif role == ID_ROLE:
            self.items[index.row()]['id'] = value
            self.dataChanged.emit(index, index)
            return True
        elif role == AGE_ROLE:
            self.items[index.row()]['priority'] = value
            self.dataChanged.emit(index, index)
            return True
        else:
            return False

    def sort(self, index, reverse):
        if index == 0:
            self.items = sorted(self.items, key=lambda x: x['name'], reverse=reverse)
        elif index == 1:
            self.items = sorted(self.items, key=lambda x: x['id'], reverse=reverse)
        elif index == 2:
            self.items = sorted(self.items, key=lambda x: x['priority'], reverse=reverse)
        self.refreshItems()

class Example(QtGui.QDialog):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.tv = QtGui.QTreeView()
        self.tv.setSortingEnabled(True)
        self.tv.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)

        customModel = CustomListModel(self, data=DATA)
        customModel.setHeaderData(0, QtCore.Qt.Horizontal, 'Name')
        customModel.setHeaderData(1, QtCore.Qt.Horizontal, 'ID')
        customModel.setHeaderData(2, QtCore.Qt.Horizontal, 'Priority')
        customModel.horizontalHeaderItem(0).setTextAlignment(QtCore.Qt.AlignCenter)
        customModel.horizontalHeaderItem(1).setTextAlignment(QtCore.Qt.AlignCenter)
        customModel.horizontalHeaderItem(2).setTextAlignment(QtCore.Qt.AlignCenter)
        self.tv.setModel(customModel)

        listDelegate = CustomListDelegate()
        self.tv.setItemDelegate(listDelegate)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.tv)
        self.setLayout(hbox)

        self.setWindowTitle('List View')
        self.resize(350, 500)
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ui = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()