import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

RU_ALF = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯ"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки',
                                                    'вид помола', 'описание вкуса', 'цена', 'объем упаковки'])
        self.show_button.clicked.connect(self.refresh_list)
        self.add_button.clicked.connect(self.show_addform)

    def show_addform(self):
        add_window.show()

    def refresh_list(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute(f"""SELECT * from coffee_table""").fetchall() #вывод всего из БД
        con.close()
        for row_data in result:
            row_number = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))


class AddWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)


if __name__ == '__main__':
    from PyQt5 import QtCore, QtWidgets

    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    ex = MainWindow()
    add_window = AddWindow()
    ex.show()
    sys.exit(app.exec())



