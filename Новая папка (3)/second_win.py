from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
from instr import *
from final_win import *
 
class TestWin(QWidget):
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
        self.txt_name = QLabel(txt_name)
        self.txt_hintname = QLineEdit(txt_hintname)
 
        self.txt_age = QLabel(txt_age)
        self.txt_hintage = QLineEdit(txt_hintage)
 
        self.txt_test1 = QLabel(txt_test1)
        self.txt_starttest1 = QPushButton(txt_starttest1)
        self.txt_hinttest1 = QLineEdit(txt_hinttest1)
 
        self.txt_test2 = QLabel(txt_test2)
        self.txt_timer = QLabel(txt_timer)
        self.txt_starttest2 = QPushButton(txt_starttest2)
 
        self.txt_test3 = QLabel(txt_test3)
        self.txt_starttest3 = QPushButton(txt_starttest3)
        self.txt_hinttest2 = QLineEdit(txt_hinttest2)
        self.txt_hinttest3 = QLineEdit(txt_hinttest3)
        self.txt_sendresults = QPushButton(txt_sendresults)
 
        self.h_line = QHBoxLayout()
        self.v_line = QVBoxLayout()
        self.v2_line = QVBoxLayout()
        self.v_line.addWidget(self.txt_name, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.txt_hintname, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.txt_age, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.hintage, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.txt_text1, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.txt_starttest1, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.txt_hinttest1, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.txt_test2, alignment = Qt.AlignLeft)
        self.v2_line.addWidget(self.txt_timer, alignment = Qt.AlignRight)
        self.v_line.addWidget(self.txt_starttest2, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.txt_test3, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.txt_starttest3, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.txt_hinttese2, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.txt_hinttest3, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.txt_sendresults, alignment = Qt.AlignCenter)
 
        self.h_line.addLayout(v_line)
        self.h_line.addLayout(v2_line)
        self.setLayout(h_line)
    def timer_tese(self):
        global time
        time = (0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.test_timer.setText(time.toString('hh:mm:ss'))
        self.test_timer.setFont(QFont('Times', 36, QFont.Bold))
        self.test_timer.setStyleSheet('color : rgb(0, 0, 0')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    
    def connects():
        self.txt_sendresults.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = FinalWin()
   