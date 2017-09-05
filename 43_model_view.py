import sys
from PySide import QtCore, QtGui

class CustomListModel(QtCore.QAbstractListModel):
    def __init__(self, parent = None, data = []):
        super(CustomListModel, self).__init__(parent)
        self.__items = data

    def rowCount(self, parent = QtCore.QModelIndex()):
        return len(self.__items)

    def data(self, index, role = QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None
        if not 0 <= index.row() < len(self.__items):
            return None
        if role == QtCore.Qt.DisplayRole:
            return self.__items[index.row()].get("name")
        elif role == QtCore.Qt.ForegroundRole:
            color = self.__items[index.row()].get("color", [])
            return QtGui.QColor(*color)
        else:
            return None

    def setData(self, index, value, role = QtCore.Qt.EditRole):
        if not index.isValid() or not 0 <= index.row() < len(self.__items):
            return False
        if role == QtCore.Qt.EditRole and value != "":
            self.__items[index.row()]["name"] = value
            self.dataChanged.emit(index, index)
            return True
        else:
            return False

    def flags(self, index):
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable

def main():
    app = QtGui.QApplication(sys.argv)
    data = [
        {"name":"Dog", "color":[255, 0, 0]},
        {"name":"Cat", "color":[0, 0, 255]}
    ]
    myListModel = CustomListModel(data = data)
    myListView = QtGui.QListView()
    myListView.setModel(myListModel)
    myListView.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()