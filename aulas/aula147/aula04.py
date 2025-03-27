"""Básico sobre Signal e Slots (eventos e documentação)"""

from PySide6.QtCore import Slot  # type: ignore
from PySide6.QtWidgets import QApplication, QGridLayout, QMainWindow, QPushButton, QWidget   # type: ignore
import sys


# Slots
@Slot()
def change_status(status_bar):
    def inner():
        status_bar.showMessage('Hello, World!')
    return inner


@Slot()
def check_action(action):
    def inner():
        print('Ação checada!' if action.isChecked() else 'Ação deschecada!')
    return inner


@Slot()
def check_click(action):
    def inner():
        print('Botão clicado!')
        action.setChecked(not action.isChecked())
    return inner


# App
app = QApplication(sys.argv)

window = QMainWindow()
central = QWidget()
window.setCentralWidget(central)
window.setWindowTitle('Bagulho doidão')

menu = window.menuBar()
option = menu.addMenu('Opção')
action = option.addAction('Ação')
another_action = option.addAction('Outra Ação')
another_action.setCheckable(True)

status = window.statusBar()
status.showMessage('Showzão de bola!')

layout = QGridLayout()
central.setLayout(layout)

btn = QPushButton('Butão')
btn.setStyleSheet('font-size: 60px;')

btn2 = QPushButton('Oto Butão')
btn2.setStyleSheet('font-size: 30px;')

btn3 = QPushButton('Mais um Butão')
btn3.setStyleSheet('font-size: 30px;')

layout.addWidget(btn, 1, 1)
layout.addWidget(btn2, 1, 2)
layout.addWidget(btn3, 2, 1, 1, 2)

action.triggered.connect(change_status(status))
another_action.hovered.connect(lambda: print(
    'Marcada!' if another_action.isChecked() else 'Desmarcada!'))
another_action.toggled.connect(check_action(another_action))
btn.clicked.connect(check_click(another_action))

window.show()
app.exec()
