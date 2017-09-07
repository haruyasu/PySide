import sys, os
from PySide import QtCore, QtGui

CURRENT_PATH = os.path.dirname(__file__)

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
            return self.__items[index.row()].get("name", "")
        elif role == QtCore.Qt.ForegroundRole:
            color = self.__items[index.row()].get("color", [])
            return QtGui.QColor(*color)
        elif role == QtCore.Qt.UserRole:
            return self.__items[index.row()].get("thumbnail", "")
        else:
            return None

    def flags(self, index):
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled

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

class CustomListDelegate(QtGui.QStyledItemDelegate):
    def __init__(self, parent=None):
        super(CustomListDelegate, self).__init__(parent)

    def paint(self, painter, option, index):
        THUMB_WIDTH = 60
        MARGIN = 5
        if option.state & QtGui.QStyle.State_Selected:
            bgBrush = QtGui.QBrush(QtGui.QColor(60, 60, 60))
            bgPen = QtGui.QPen(QtGui.QColor(60, 60, 60), 0.5, QtCore.Qt.SolidLine)
            painter.setPen(bgPen)
            painter.setBrush(bgBrush)
            painter.drawRect(option.rect)

        name = index.data(QtCore.Qt.DisplayRole)
        color = index.data(QtCore.Qt.ForegroundRole)
        thumbName = index.data(QtCore.Qt.UserRole)
        thumbImage = QtGui.QPixmap(os.path.join(CURRENT_PATH, "img", thumbName)).scaled(THUMB_WIDTH, THUMB_WIDTH)
        r = QtCore.QRect(option.rect.left(), option.rect.top(), THUMB_WIDTH, THUMB_WIDTH)
        painter.drawPixmap(r, thumbImage)

        pen = QtGui.QPen(color, 0.5, QtCore.Qt.SolidLine)
        painter.setPen(pen)
        #painter.drawText(option.rect, QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft, "Name : " + name)

        r = QtCore.QRect(option.rect.left() + THUMB_WIDTH + MARGIN, option.rect.top(), option.rect.width() - THUMB_WIDTH - MARGIN, option.rect.height())
        painter.drawText(r, QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft, "Name : " + name)

    def sizeHint(self, option, index):
        return QtCore.QSize(100, 60)

def main():
    app = QtGui.QApplication(sys.argv)
    data = [
        {"name":"Dog", "color": [255, 0, 0], "thumbnail": "ben.png"},
        {"name":"Cat", "color": [0, 0, 255], "thumbnail": "natalie.png"}
    ]
    myListModel = CustomListModel(data = data)
    myListView = QtGui.QListView()
    myListView.setModel(myListModel)
    myListDelegate = CustomListDelegate()
    myListView.setItemDelegate(myListDelegate)
    myListView.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()