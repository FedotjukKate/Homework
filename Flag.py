import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtWidgets import QMainWindow, QRadioButton
from ui_flag import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.ok)

    def ok(self):
        result = []
        if self.radioButton_1_red.isChecked():
            result.append("Красный")
        elif self.radioButton_1_green.isChecked():
            result.append("Зеленый")
        else:
            result.append("Синий")

        if self.radioButton_2_red.isChecked():
            result.append("Красный")
        elif self.radioButton_2_green.isChecked():
            result.append("Зеленый")
        else:
            result.append("Синий")

        if self.radioButton_3_red.isChecked():
            result.append("Красный")
        elif self.radioButton_3_green.isChecked():
            result.append("Зеленый")
        else:
            result.append("Синий")

        self.label_4.setText(", ".join(result))






sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook


if __name__ == '__main__':
    # Создадим класс приложения PyQT
    app = QApplication(sys.argv)
    # А теперь создадим и покажем пользователю экземпляр
    # нашего виджета класса Example
    ex = MainWindow()
    ex.show()
    # Будем ждать, пока пользователь не завершил исполнение QApplication,
    # а потом завершим и нашу программу
    sys.exit(app.exec())