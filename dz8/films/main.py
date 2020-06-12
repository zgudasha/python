import sys
import sqlite3
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow, QDialog, QMessageBox, QErrorMessage
from films import Ui_MainWindow
from dialog import Ui_Form


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dialog = DialogAdd()

        self.con = sqlite3.connect('films.db')
        self.cur = self.con.cursor()

        self.genres = dict(self.cur.execute(f"""SELECT * FROM "genres" """).fetchall()) # fetchall -> список картежей (id, название)
        self.list.addItems(self.genres.values()) # добавляем в список фильмов только значения из словаря self.genres

        self.genre = 0 # когда жанр не выбран
        self.list.itemClicked.connect(self.changeGenre) # по клику на элемент списка меняется self.genre
        self.btnSearch.clicked.connect(self.getFilms) # отбирает фильмы по критериям
        self.btnSave.clicked.connect(self.save) # сохранение изменений 
        self.btnAdd.clicked.connect(self.openDialog) 

    def save(self):
        for i in range(self.table.rowCount()):
            row = []
            for j in range(self.table.columnCount()): # бежим по ряду и добавляем элементы
                row.append(self.table.item(i, j).text())

            id_, title, year, genre, duration = row

            self.cur.execute(
                f"""
                UPDATE "Films" 
                SET title = "{title}", 
                    year = "{year}", 
                    genre = "{genre}",
                    duration = "{duration or 0}"
                WHERE id = "{id_}"
                """)
        self.con.commit() # сохряняем изменения в базе данных

    def openDialog(self):
        self.dialog.show()
        self.dialog.ok.clicked.connect(self.add)
        self.dialog.cancel.clicked.connect(self.closeDialog)

    def closeDialog(self):
        self.dialog.close()

    def add(self):
        title = self.dialog.title.toPlainText()
        year = self.dialog.year.toPlainText()
        genre = self.dialog.genre.toPlainText()
        duration = self.dialog.duration.toPlainText()
        self.closeDialog()
        # если жанр корректный и остаальное введено
        if genre in self.genres.values() and title and year and genre and duration:
            for key, value in self.genres.items():
                if value == genre:
                    genre = key # берем id от значения
        else:
            return
        self.cur.execute(
            f"""
            INSERT INTO "Films"(title, year, genre, duration) VALUES("{title}", {year}, {genre}, {duration})
            """
        )
        self.con.commit()


    def changeGenre(self, item):
        title = item.text()
        for key, value in self.genres.items():
            if value == title:
                self.genre = key

    def getFilms(self):
        title = self.titleField.toPlainText().strip()
        year = self.yearField.toPlainText().strip()
        duration = self.durationField.toPlainText().strip()

        if not self.genre: # когда жанр не выбран
            genre = f'(genre <= {max(self.genres.keys())})'
        else:
            genre = f'(genre = {self.genre})'

        if title:
            title = f' AND (title like "%{title}%")'
        else:
            title = ''

        if year:
            year = f' AND (year = {year})'
        else:
            year = ''

        if duration:
            duration = f' AND (duration = {duration})'
        else:
            duration = ''
        
        r = self.cur.execute(f"""SELECT * FROM Films WHERE {genre + title + year + duration}""").fetchall()
        if r:
            self.loadTable(r)
        else:
            self.clearTable()

    def loadTable(self, result):
        self.clearTable()
        self.table.setColumnCount(len(result[0]))
        for i, row in enumerate(result):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j, col in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(col)))
            self.table.item(i, 0).setFlags(Qt.ItemIsEnabled) # нельзя выделять поле id

    def clearTable(self):
        self.table.setRowCount(0)
        self.table.setColumnCount(0)


class DialogAdd(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
