import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки',
                                                    'вид помола', 'описание вкуса', 'цена', 'объем упаковки'])
        self.show_button.clicked.connect(self.refresh_list)
        self.tableWidget.itemSelectionChanged.connect(self.activate_updater)
        self.delete_button.clicked.connect(self.delete_or_insert)
        self.add_button.clicked.connect(self.show_addform)

    def show_addform(self):
        add_window.show()

    def refresh_list(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute(f"""SELECT * from coffee_table""").fetchall() #вывод всего из БД
        con.close()
        self.tableWidget.setRowCount(0)
        for row_data in result:
            row_number = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))

    def activate_updater(self):
        sen = self.sender()
        if sen.currentRow() is not None:
            self.row_current = sen.currentRow()
            self.delete_button.setEnabled(True)
            self.delete_button.setText(f"Изменить строку {sen.currentRow() + 1}")
        else:
            self.delete_button.setEnabled(False)

    def delete_or_insert(self):
        pass

class AddWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.cancelButton.clicked.connect(self.cancel)
        self.addButton.clicked.connect(self.button_add)
        self.lineEdit_list = [self.lineEdit_sort,
                             self.lineEdit_degree,
                             self.lineEdit_forma,
                             self.lineEdit_description,
                             self.lineEdit_price,
                             self.lineEdit_size]
        for line in self.lineEdit_list:
            line.textChanged.connect(self.button_enabler)

    def cancel(self):
        self.close()

    def button_enabler(self):
        if all(map(lambda x: x.text().strip(), self.lineEdit_list)) and \
                self.lineEdit_degree.text().strip().isdigit() and \
                self.is_number(self.lineEdit_price.text().strip()) and \
                self.is_number(self.lineEdit_size.text().strip()):
            self.addButton.setEnabled(True)
        else:
            self.addButton.setEnabled(False)

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def button_add(self):
        sort = self.lineEdit_sort.text()
        degree = int(self.lineEdit_degree.text())
        forma = self.lineEdit_forma.text()
        description = self.lineEdit_description.text()
        price = self.lineEdit_price.text()
        size = self.lineEdit_size.text()
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        cur.execute(f"""INSERT INTO coffee_table(sort, degree, forma, description, price, size)
                                VALUES ({sort}, {degree}, {forma}, {description}, {price}, {size})""")
        con.commit()
        con.close()
        for i in self.lineEdit_list:
            i.setText("")
        ex.refresh_list()


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



