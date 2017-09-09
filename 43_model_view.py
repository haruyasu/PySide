import sys, os
from PySide import QtCore, QtGui

CURRENT_PATH = os.path.dirname(__file__)

DESCRIPTION_ROLE = QtCore.Qt.UserRole
STATUS_ROLE = QtCore.Qt.UserRole + 1
THUMB_ROLE = QtCore.Qt.UserRole + 2

DATA = [
    {"name": "Dog", "description": "Animal", "status": "OK", "color": [255, 0, 0], "thumbnail": "ben.png"},
    {"name": "Cat", "description": "Animal", "status": "OK", "color": [0, 0, 255], "thumbnail": "natalie.png"}
]

class CustomListModel(QtCore.QAbstractListModel):
    def __init__(self, parent = None, data = None):
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
            return self.__items[index.row()]["name"]
        elif role == DESCRIPTION_ROLE:
            return self.__items[index.row()]["description"]
        elif role == STATUS_ROLE:
            return self.__items[index.row()]["status"]
        elif role == THUMB_ROLE:
            return self.__items[index.row()]["thumbnail"]
        elif role == QtCore.Qt.BackgroundRole:
            color = self.__items[index.row()]["color"]
            return QtGui.QColor(color[0], color[1], color[2])
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

class GUI(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)
        self.setWindowTitle('Model View Delegate')
        self.resize(350, 600)
        self.setMaximumSize(525, 700)
        self.initUI()

    def initUI(self):
        myListView = QtGui.QListView(self)
        myListView.setSpacing(10)
        myListView.setAutoFillBackground(False)
        url = os.path.join(CURRENT_PATH, "img", "bg.png").replace("\\", "/")
        myListView.setStyleSheet("background: url(" + url + ") center center;")
        myListView.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)

        myListModel = CustomListModel(data=DATA)

        myListDelegate = CustomListDelegate()

        myListView.setModel(myListModel)
        myListView.setItemDelegate(myListDelegate)

        self.setCentralWidget(myListView)

def main():
    app = QtGui.QApplication(sys.argv)
    ui = GUI()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()