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
        inst = QLabel('Здесь инструкция')
        button = QPushButton('Кнопка для нажатия')
        v_line = QVBoxLayout()

    def connects(self):
        pass

if __name__ == '__main__':
    app = QApplication([])
    main = MainWin()
    app.exec_()