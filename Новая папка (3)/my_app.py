from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout
from instr import *
from second_win import *
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.txt_hello = QLabel(txt_hello)
        self.txt_instruction = QLabel(txt_instruction)
        self.txt_next = QPushButton(txt_next)
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.txt_hello, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.txt_next, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.txt_instruction, alignment = Qt.AlignCenter)
        self.setLayout(self.v_line)
    def connects(self):
        self.txt_next.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = TestWin()
app = QApplication([])
main_win = MainWin()
app.exec_()