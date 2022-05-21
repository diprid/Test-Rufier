from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit

from PyQt5.QtCore import Qt, QTime, QTimer

from PyQt5.QtGui import QIntValidator, QDoubleValidator

from PyQt5.QtCore import QLocale

class Experiment():
    def __init__(self, age, p1, p2, p3):
        self.age = age
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def result(self):
        self.index = (4 * (self.p1+ self.p2+ self.p3) - 200) / 10
        if self.age < 7:
            self.recomen = ' Нет результатов для данного возраста'
        if self.age >= 7 or self.age == 8:
            if self.index > 21:
                self.recomen = ' низкая. Срочно обратитесь к врачу!'
            elif self.index >= 17 and self.index < 21:
                self.recomen = ' удовлетворительная. Обратитесь к врачу!'
            elif self.index >= 12 and self.index < 17:
                self.recomen = ' средняя. Возможно, стоит дополнительно обследоваться у врача.'
            elif self.index >= 6.5 and self.index < 12:
                self.recomen = ' выше среднего'
            else:
                self.recomen = ' высокая'

        if self.age >= 9 or self.age == 10:
            if self.index > 19.5:
                self.recomen = ' низкая. Срочно обратитесь к врачу!'
            elif self.index >= 15.5 and self.index < 19.4:
                self.recomen = ' удовлетворительная. Обратитесь к врачу!'
            elif self.index >= 10.5 and self.index < 15.4:
                self.recomen = ' средняя. Возможно, стоит дополнительно обследоваться у врача.'
            elif self.index >= 5 and self.index < 10.4:
                self.recomen = ' выше среднего'
            else:
                self.recomen = ' высокая'

        if self.age >= 11 or self.age == 12:
            if self.index > 18:
                self.recomen = 'низкая. Срочно обратитесь к врачу!'
            elif self.index >= 14 and self.index < 17.9:
                self.recomen = 'удовлетворительная. Обратитесь к врачу!'
            elif self.index >= 9 and self.index < 13.9:
                self.recomen = 'средняя. Возможно, стоит дополнительно обследоваться у врача.'
            elif self.index >= 3.5 and self.index < 8.9:
                self.recomen = 'выше среднего'
            else:
                self.recomen = 'высокая'

        if self.age >= 15:
            if self.index > 15:
                self.recomen = 'низкая. Срочно обратитесь к врачу!'
            elif self.index >= 11 and self.index < 14.9:
                self.recomen = 'удовлетворительная. Обратитесь к врачу!'
            elif self.index >= 6 and self.index < 10.9:
                self.recomen = 'средняя. Возможно, стоит дополнительно обследоваться у врача.'
            elif self.index >= 0.5 and self.index < 5.9:
                self.recomen = 'выше среднего'
            else:
                self.recomen = 'высокая'

        if self.age >= 7 or self.age == 8:
            if self.index > 21:
                self.recomen = 'низкая. Срочно обратитесь к врачу!'
            elif self.index >= 17 and self.index < 21:
                self.recomen = 'удовлетворительная. Обратитесь к врачу!'
            elif self.index >= 12 and self.index < 17:
                self.recomen = 'средняя. Возможно, стоит дополнительно обследоваться у врача.'
            elif self.index >= 6.5 and self.index < 12:
                self.recomen = 'выше среднего'
            else:
                self.recomen = 'высокая'


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
        Hey = QLabel('Здравствуй!')
        instr = QLabel('Это приложение для того чтобы измерить работу сердца')
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
        label_age = QLabel('Возраст')
        self.age = QLineEdit('')
        age = QLocale(QLocale.English, QLocale.UnitedStates)
        validator = QDoubleValidator()
        validator.setLocale(age)
        self.age.setValidator(validator)

        instr1 = QLabel('''Лягте на спину и замерьте пульс за 15 секунд. 
        Нажмите кнопку "Начать первый тест", чтобы запустить таймер. Результат запишите в соответствующее поле''')
        self.test1 = QPushButton('Начать первый тест')
        self.p1 = QLineEdit('')
        self.p1.setValidator(validator)
        instr2 = QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",чтобы запустить счетчик приседаний')
        self.test2 = QPushButton('2 Тест')
        instr3 = QLabel('''Лягте на спину и замерьте пульс сначала за  первые 15 секунд минуты, затем за последние 15 секунд. 
        Нажмите кнопку "Начать финальный тест", чтобы запустить таймер. Зеленым обозначены секунды, 
        в течение которых необходимо проводить изменения, черным - минуты без замера пульсаций. Результаты запишите в соответствующие поля.''')
        self.test3 = QPushButton('3 Тест')
        self.p2 = QLineEdit('')
        self.p2.setValidator(validator)
        self.p3 = QLineEdit('')
        self.p3.setValidator(validator)
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
        self.test1.clicked.connect(self.timer1)
        self.test2.clicked.connect(self.timer2)
        self.test3.clicked.connect(self.timer3)

    def timer1(self):
        self.timer = QTimer()
        self.time = QTime(0, 0, 16)
        self.timer.timeout.connect(self.event1)
        self.timer.start(1000)

    def event1(self):
        self.time = self.time.addSecs(-1)
        self.label_timer.setText(self.time.toString('hh:mm:ss'))
        if self.time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer2(self):
        self.timer = QTimer()
        self.time = QTime(0, 0, 31)
        self.timer.timeout.connect(self.event2)
        self.timer.start(2000)

    def event2(self):
        self.time = self.time.addSecs(-1)
        self.label_timer.setText(self.time.toString('hh:mm:ss')[6:8])
        if self.time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer3(self):
        self.timer = QTimer()
        self.time = QTime(0, 0, 31)
        self.timer.timeout.connect(self.event3)
        self.timer.start(2000)

    def event3(self):
        self.time = self.time.addSecs(-1)
        self.label_timer.setText(self.time.toString('hh:mm:ss'))
        if int(self.time.toString('hh:mm:ss')[6:8]) < 59 and int (self.time.toString('hh:mm:ss')[6:8]) > 45:
            self.label_timer.setStyleSheet('color:rgb(0,255,0)')
        elif int(self.time.toString('hh:mm:ss')[6:8]) < 45 and int(self.time.toString('hh:mm:ss')[6:8]) > 15:
            self.label_timer.setStyleSheet('color:rgb(0,0,0)')
        else:
            self.label_timer.setStyleSheet('color:rgb(0,255,0)')
        if self.time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def next(self):
        exp = Experiment(int(self.age.text()), int(self.p1.text()), int(self.p2.text()), int(self.p3.text()))
        exp.result()
        tried.setResult(exp.index, exp.recomen)
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
    def setResult(self, index, recomen):
        self.index.setText('Ваш индекс:' + str(index))
        self.recomen.setText('Ваш уровень работы сердца: ' + recomen)

if __name__ == '__main__':
    app = QApplication([])
    main = MainWin()
    second = TestWin()
    tried = FinalWin()
    app.exec_()