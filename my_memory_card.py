#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,QLabel,QHBoxLayout, QRadioButton, QMessageBox,QGroupBox, QButtonGroup
from random import shuffle, randint
#создание приложения и главного окна
app = QApplication([])
win = QWidget()

win.setWindowTitle('Розыгрыш')
btn_ok = QPushButton('Ответить')
lb_question = QLabel('Когда я родился?')

class Question():
    def __init__(self,question,right_ans,wrong1,wrong2,wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        



radio_group_box = QGroupBox('Варианты ответов:')
btn_ans1 = QRadioButton('1953')
btn_ans2 = QRadioButton('2019')
btn_ans3 = QRadioButton('2007')
btn_ans4 = QRadioButton('2005')

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_ans1)
RadioGroup.addButton(btn_ans2)
RadioGroup.addButton(btn_ans3)
RadioGroup.addButton(btn_ans4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(btn_ans1)
layout_ans2.addWidget(btn_ans2)
layout_ans3.addWidget(btn_ans3)
layout_ans3.addWidget(btn_ans4)





layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

radio_group_box.setLayout(layout_ans1)


AnsGroupBox = QGroupBox('Результат теста')
lb_result = QLabel('праавильно')
lb_Correct = QLabel('1953')



layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft|Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter,stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)



layout_line1.addWidget(lb_question, alignment = Qt.AlignHCenter|Qt.AlignVCenter)
layout_line2.addWidget(radio_group_box)
layout_line2.addWidget(AnsGroupBox)
radio_group_box.show()
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)


layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2,stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3,stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
# Вся программа остальная с первого урока



win.setLayout(layout_card)
win.setWindowTitle('Memory card')


def show_result():
    radio_group_box.hide()
    AnsGroupBox.show()
    btn_ok.setText('След вопрос')

def show_question():
    radio_group_box.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn_ans1.setChecked(False)
    btn_ans2.setChecked(False)
    btn_ans3.setChecked(False)
    btn_ans4.setChecked(False)
    RadioGroup.setExclusive(True)

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_Correct.setText(q.right_ans)
    show_question()

question_list = []
question_list.append(Question('Когда я родился', '2007', '42425', '1953', '2005'))
question_list.append(Question('Что я вчера делал?', 'гулял', 'собака','ничего','спал'))
question_list.append(Question('Чем я занимаюсь каждый день?','играю','программирую','учусь','каждый день'))

win.score = 0
win.total = 0
def next_question():
    win.total+=1
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)
    
    

def test():
    if 'Ответить' == btn_ok.text():
        check_answer()
    else:
        next_question()


answers = [btn_ans1, btn_ans2, btn_ans3, btn_ans4]

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        win.score +=1
        
        
    else:
        if answers[1].isChecked or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно')
    print('Статистика:\n-Всего вопросов',win.total , 'Правильных ответов:', win.score)
    print('Рейтинг:',int((win.score/win.total)*100),'%')



btn_ok.clicked.connect(test)



win.resize(400,600)
next_question()
win.show()
app.exec()
