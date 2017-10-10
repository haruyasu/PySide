__appname__ = "PyDataMan"
__modlule__ = "main"

from PySide.QtCore import *
from PySide.QtGui import *
import sys, sqlite3, re, os, logging
from ui import mainWindw_PyDataMan

appDataPath = os.environ["APPDATA"] + "\\PyDataMan\\"

if not os.path.exists(appDataPath):
    try:
        os.makedirs(appDataPath)
    except Exception, e:
        appDataPath = os.getcwd()

logging.basicConfig(filename=appDataPath + "pydataman.log",
                    format="%(asctime)-15s: %(name)-18s - %(levelname)-8s - %(module)-15s - %(funcName)-20s - %(lineno)-6d - %(message)s")

logger = logging.getLogger(name="main-gui")

class Main(QMainWindow, mainWindw_PyDataMan.Ui_mainWindow):
    dbPath = appDataPath + "pydata.db"
    dbConn = sqlite3.connect(dbPath)

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.dbCursor = self.dbConn.cursor()
        self.dbCursor.execute("""CREATE TABLE IF NOT EXISTS Main(id INTEGER PRIMARY KEY,
                                 username TEXT, name TEXT, phone TEXT, addresss TEXT, status TEXT""")
        self.dbConn.commit()

        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope, "PyDataMan", "PyDataMan")

    def load_initial_settings(self):
        """Loads the initial settings for the application. Sets the mainTable colum widths."""
        pass

    def add_button_clicked(self):
        """Calls the validate_fields() method, and adds the items to the table if true"""
        pass

    def remove_row_clicked(self):
        """Removes the selected row from the mainTable"""
        pass

    def validate_fields(self):
        """Validated the QLineEdits based on RegEx"""
        pass

    def import_action_triggered(self):
        """Database import handler"""
        pass

    def export_action_triggered(self):
        """Database export handler"""
        pass

    def preferences_action_trigggered(self):
        """Fires up the Preferences dialog"""
        pass

    def about_action_triggered(self):
        """Opens the About dialog"""
        pass

    def exit_action_triggered(self):
        """Closes the application"""
        pass

def main():
    QCoreApplication.setApplicationName("PyDataMan")
    QCoreApplication.setApplicationVersion("0.1")
    QCoreApplication.setOrganizationName("PyDataMan")
    QCoreApplication.setOrganizationDomain("pydataman.com")

    app = QApplication(sys.argv)
    form =Main()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()
