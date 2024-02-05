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
        self.update_button.clicked.connect(self.show_updateform)
        self.add_button.clicked.connect(self.show_addform)
        self.delete_button.clicked.connect(self.delete_btn)

    def show_addform(self):
        add_window.show()

    def show_updateform(self):
        datarow = list(map(lambda x: x.text(), self.tableWidget.selectedItems()))
        update_window.fillForm(datarow)
        update_window.show()

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
        self.update_button.setEnabled(False)
        self.update_button.setText(f"Изменить")

    def activate_updater(self):
        sen = self.sender()
        if self.tableWidget.selectedItems():
            self.row_current = sen.currentRow()
            self.update_button.setEnabled(True)
            self.delete_button.setEnabled(True)
            self.update_button.setText(f"Изменить строку {sen.currentRow() + 1}")
            self.delete_button.setText(f"Удалить строку {sen.currentRow() + 1}")
        else:
            self.update_button.setEnabled(False)
            self.delete_button.setEnabled(False)
            self.update_button.setText(f"Изменить")
            self.delete_button.setText(f"Удалить")

    def delete_btn(self):
        del_id = int(self.tableWidget.selectedItems()[0].text())
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        cur.execute(f"""DELETE FROM coffee_table
                        WHERE id = {del_id}""")
        con.commit()
        con.close()
        self.refresh_list()


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


class UpdateWindow(AddWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.cancelButton.clicked.connect(self.cancel)
        self.addButton.clicked.connect(self.UpdateButton)
        self.addButton.setText("Внести изменения")
        self.lineEdit_list = [self.lineEdit_sort,
                              self.lineEdit_degree,
                              self.lineEdit_forma,
                              self.lineEdit_description,
                              self.lineEdit_price,
                              self.lineEdit_size]
        for line in self.lineEdit_list:
            line.textChanged.connect(self.button_enabler)

    def UpdateButton(self):
        sort = self.lineEdit_sort.text()
        degree = int(self.lineEdit_degree.text())
        forma = self.lineEdit_forma.text()
        description = self.lineEdit_description.text()
        price = self.lineEdit_price.text()
        size = self.lineEdit_size.text()
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        cur.execute(f"""UPDATE coffee_table
                        SET sort = '{sort}', 
                            degree = {degree}, 
                            forma = '{forma}', 
                            description = '{description}', 
                            price = '{price}', 
                            size = '{size}'
                        WHERE id = {self.id}
                        """)
        con.commit()
        con.close()
        ex.refresh_list()

    def fillForm(self, datarow):
        self.id = int(datarow[0])
        for i in range(len(self.lineEdit_list)):
            self.lineEdit_list[i].setText(datarow[i + 1])


if __name__ == '__main__':
    from PyQt5 import QtCore, QtWidgets

    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    ex = MainWindow()
    add_window = AddWindow()
    update_window = UpdateWindow()
    ex.show()
    sys.exit(app.exec())



