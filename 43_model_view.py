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

class CustomListDelegate(QtGui.QStyledItemDelegate):

    ITEM_SIZE_HINT = [300, 70]
    MARGIN = 20
    THUMB_AREA_WIDTH = 70
    THUMB_WIDTH = 60
    STATUS_AREA_WIDTH = 24
    BG_DEFAULT = QtGui.QBrush(QtGui.QColor(247, 248, 242))
    BG_SELECTED = QtGui.QBrush(QtGui.QColor(255, 255, 204))
    BORDER_DEFAULT = QtGui.QPen(QtGui.QColor(255, 255, 255), 0.5, QtCore.Qt.SolidLine)
    TEXT_BLACK_PEN = QtGui.QPen(QtGui.QColor(106, 107, 109), 0.5, QtCore.Qt.SolidLine)
    SHADOW_PEN = QtGui.QPen(QtGui.QColor(220, 220, 220, 100), 1, QtCore.Qt.SolidLine)
    FONT_H1 = QtGui.QFont("Corbel", 12, QtGui.QFont.Normal, True)
    FONT_H2 = QtGui.QFont("Corbel", 11, QtGui.QFont.Normal, True)

    def __init__(self, parent=None):
        super(CustomListDelegate, self).__init__(parent)

    def paint(self, painter, option, index):
        selected = False

        if option.state & QtGui.QStyle.State_Selected:
            selected = True

        name = index.data(QtCore.Qt.DisplayRole)
        description = index.data(DESCRIPTION_ROLE)
        status = index.data(STATUS_ROLE)
        color = index.data(QtCore.Qt.BackgroundRole)
        thumbnail = index.data(THUMB_ROLE)

        self.drawBackground(painter, option.rect, selected, color)
        self.drawThumbnail(painter, option.rect, thumbnail)
        self.drawName(painter, option.rect, name)
        self.drawDescription(painter, option.rect, description)
        self.drawStatus(painter, option.rect, status)

    def sizeHint(self, option, index):
        return QtCore.QSize(self.ITEM_SIZE_HINT[0], self.ITEM_SIZE_HINT[1])

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