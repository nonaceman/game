import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox, QGridLayout
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import QFont

class MoneyGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Игра с кнопками')
        self.setGeometry(100, 100, 800, 600)

        #Фиксированные суммы
        self.amounts = [1, 10, 15, 1000, 10000, 25000, 50000, 75000, 100000, 150000, 250000, 300000, 1000000, 2000000, 3000000]
        random.shuffle(self.amounts)

        #Создание кнопок
        self.buttons = []
        layout = QGridLayout()
        for i in range(15):
            button = QPushButton(f'Кнопка {i+1}', self)
            button.clicked.connect(lambda checked, idx=1: self.on_button_click(idx))
            font = QFont("Arial", 14)
            button.setMinimumSize(120, 60)
            self.buttons.append(button)
            row = i//5
            col = i%5
            layout.addWidget(button, row, col)
            
        #Созхдание списка оставшизся сумм
        self.amount_list_label = QLabel(self)
        self.amount_list_label.setFont(QFont("Arial", 12))
        self.update_amount_list()
        layout.addWidget(self.amount_list_label)

        self.setLayout(layout)

    def on_button_click(self, index):
        button = self.buttons[index]
        amount = self.amounts[index]
        self.amounts[index] = None #Удаляем сумму из списка
        self.update_amount_list()

        #Красим кнопку в красный и делаем её неактивной
        button.setStyleSheet("background-color: red; color: white;")
        button.setEnabled(False)

        #Показываем сообщение
        QMessageBox.information(self, 'Результат', f'Вы проиграли {amount} рублей')

        #Проверка окончания игры
        if all(a is None for a in self.amounts):
            remaining_amount = [a for a in self.amounts if a is not None][0]
            QMessageBox.information(self, 'Вы выиграли!', f'Вы выиграли {remaining_amount} рублей')
            self.close()

    def update_amount_list(self):
        remaining_amounts = [str(a) for a in self.amounts if a is not None]
        self.amount_list_label.setText('Оставшиеся суммы:\n' + '\n'.join(remaining_amounts))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = MoneyGame()
    game.show()
    sys.exit(app.exec_())