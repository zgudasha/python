import csv
import sys
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow
from PyQt5.QtGui import QColor
from table import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadTable('results.csv')

    def loadTable(self, table_name):
        with open(table_name, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            # заголовок таблицы
            title = next(reader) + ['Итого']
            self.table.setColumnCount(len(title))
            self.table.setHorizontalHeaderLabels(title)

            # пропускаю строку с номерами заданий
            # чтобы не закрасить лишнее 
            next(reader)

            for i, row in enumerate(reader):
                # добавляем строчки(увеличиваем кол-во)
                self.table.setRowCount(self.table.rowCount() + 1)

                mark = 0

                for j, elem in enumerate(row):
                    if type(elem) is str:
                        elem = elem.replace(',', '.')

                    if j > 2:
                        elem = float(elem)
                        mark += elem
                    
                    # ставим элемент в таблицу приложения
                    self.table.setItem(i, j, QTableWidgetItem(str(elem)))

                mark = mark / (self.table.columnCount() - 4)
                # ставим итоговую оценку в последнюю колонку
                self.table.setItem(i, self.table.columnCount() - 1, QTableWidgetItem(str(mark)))

                color = (125, 125, 125)

                if mark >= 95:
                    color = (159, 201, 110)
                elif 80 <= mark < 95:
                    color = (221, 209, 103)
                elif 60 <= mark < 80:
                    color = (221, 103, 103)

                # закрашиваем ряд
                self.colorRow(i, QColor(*color))

    def colorRow(self, row, color):
        # красим каждую колонку в переданной строке
        for i in range(self.table.columnCount()):
            self.table.item(row, i).setBackground(color)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
