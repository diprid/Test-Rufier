from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit

from PyQt5.QtCore import Qt

class MainWin(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.set_appear()
        self.unitUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.resize(600, 400)
        self.setWindowTitle('Opera GX')
        self.move(400, 250)

    def unitUI(self):
        Hey = QLabel('Здесь приветствие')
        instr = QLabel('Здесь инструкция')
        self.button = QPushButton('Кнопка для нажатия')
        v_line = QVBoxLayout()
        v_line.addWidget(Hey)
        v_line.addWidget(instr)
        v_line.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(v_line)

    def connects(self):
                self.button.clicked.connect(self.next)

    def next(self):
        self.hide()
        second.show()

class TestWin(QWidget):
    def __init__(self): 
        QWidget.__init__(self)
        self.set_appear()
        self.unitUI()
        self.connects()
    def set_appear(self):
        self.resize(600, 400)
        self.setWindowTitle('Opera')
        self.move(400, 250)
    def unitUI(self):
        label_fio = QLabel('Введите ФИО')
        fio = QLineEdit()
        label_age = QLabel('Возрост')
        self.age = QLineEdit('0')
        instr1 = QLabel('Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер. Результат запишите в соответствующее поле')
        self.test1 = QPushButton('Начать первый тест')
        self.p1 = QLineEdit('0')
        instr2 = QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания", чтобы запустить счетчик приседаний')
        self.test2 = QPushButton('2 Тест')
        instr3 = QLabel('''Лягте на спину и замерьте пульс сначала за  первые 15 секунд минуты, затем за последние 15 секунд. 
        Нажмите кнопку "Начать финальный тест", чтобы запустить таймер. Зеленым обозначены секунды, в течение которых необходимо проводить изменения, черным - минуты без замера пульсаций. Результаты запишите в соответствующие поля.''')
        self.test3 = QPushButton('3 Тест')
        self.p2 = QLineEdit('0')
        self.p3 = QLineEdit('0')
        self.button = QPushButton('Завершить')
        self.label_timer = QLabel('00:00:00')
        main_line = QHBoxLayout()
        v_line1 = QVBoxLayout()
        v_line2 = QVBoxLayout()
        v_line1.addWidget(label_fio)
        v_line1.addWidget(fio)
        v_line1.addWidget(label_age)
        v_line1.addWidget(self.age)
        v_line1.addWidget(instr1)
        v_line1.addWidget(self.test1)
        v_line1.addWidget(self.p1)
        v_line1.addWidget(instr2)
        v_line1.addWidget(self.test2)
        v_line1.addWidget(instr3)
        v_line1.addWidget(self.test3)
        v_line1.addWidget(self.p2)
        v_line1.addWidget(self.p3)
        v_line1.addWidget(self.button, alignment=Qt.AlignCenter)
        v_line2.addWidget(self.label_timer)
        main_line.addLayout(v_line1)
        main_line.addLayout(v_line2)
        self.setLayout(main_line)

    def connects(self):
        self.button.clicked.connect(self.next)
    def next(self):
        self.hide()
        tried.show()

class FinalWin(QWidget):
    def __init__(self): 
        QWidget.__init__(self)
        self.set_appear()
        self.unitUI()
    def set_appear(self):
        self.resize(600, 400)
        self.setWindowTitle('Opera')
        self.move(400, 250)
    def unitUI(self):
      self.index = QLabel('index')
      self.recomen = QLabel('recom')
      v_line = QVBoxLayout()
      v_line.addWidget(self.index, alignment= Qt.AlignCenter)
      v_line.addWidget(self.recomen, alignment= Qt.AlignCenter)
      self.setLayout(v_line)

if __name__ == '__main__':
    app = QApplication([])
    main = MainWin()
    second = TestWin()
    tried = FinalWin()
    app.exec_()