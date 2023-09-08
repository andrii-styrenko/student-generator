from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])

main_win = QWidget()
main_win.resize(500,500)
main_win.setWindowTitle('Генератор студента')

button = QPushButton('Згенерувати')

text = QLabel('Натисни, щоб дізнатися хто відповідає на запитання')
winner = QLabel('?')

line = QVBoxLayout()
line.addWidget(text,alignment = Qt.AlignCenter)
line.addWidget(winner,alignment = Qt.AlignCenter)
line.addWidget(button,alignment = Qt.AlignCenter)

main_win.setLayout(line)

student_list = ['Дерипаска Матвій','Доценко Марина','Єгорова Злата','Кісельов Олександр','Коломієць Артем','Кушнір Андрій','Місяць Захар','Паламарчук Артем','Чайка Святослав']

def show_winner():
    rand_num = randint(0,8)
    for i in range(len(student_list)):
        if i == rand_num:
            winner.setText(student_list[i])
            text.setText('Відповідає:')

button.clicked.connect(show_winner)


main_win.show()
app.exec_()