from PyQt5.QtWidgets import QMainWindow 
from ui_table_window import Ui_MainWindow as Ui_TableWindow

class TableWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TableWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(["температура", "влажность", "освещение"])
