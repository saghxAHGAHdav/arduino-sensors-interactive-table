import csv
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from ui_main_window import Ui_MainWindow as Ui_MainWindowDesign
from table_window import TableWindow
from data_reader import get_data

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindowDesign()
        self.ui.setupUi(self)
        self.table_window = TableWindow()
        self.ui.readButton.clicked.connect(self.read_data)
        self.ui.tableButton.clicked.connect(self.open_table)
        self.ui.saveButton.clicked.connect(self.save_to_csv)
    def open_table(self): #МОМЕНТ ОТКРЫТИЯ ТАБЛИЦЫ
        self.table_window.show()

    def read_data(self):
        data = get_data()
        table = self.table_window.ui.tableWidget
        currrow = table.rowCount()
        table.insertRow(currrow)
        table.setItem(currrow, 0, QTableWidgetItem(str(data[0])))
        table.setItem(currrow, 1, QTableWidgetItem(str(data[1])))
        table.setItem(currrow, 2, QTableWidgetItem(str(data[2])))
            

    def save_to_csv(self):
        table = self.table_window.ui.tableWidget
        count = table.rowCount()
        with open("data.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["температура", "влажность", "освещение"])
            for row in range(count):
                temp = table.item(row, 0).text()
                hum = table.item(row, 1).text()
                ldr = table.item(row, 2).text()
                writer.writerow([temp, hum, ldr])
                    
