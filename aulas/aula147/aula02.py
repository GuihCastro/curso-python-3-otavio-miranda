"""`QWidget` e `QLayout` de `PySide6.QtWidgets"""
# `QWidget` -> genérico
# `QLayout` -> Um widget de layout que recebe outros widgets

from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget   # type: ignore
import sys

app = QApplication(sys.argv)

window = QWidget()

layout = QGridLayout()
window.setLayout(layout)

btn = QPushButton('Butão')
btn.setStyleSheet('font-size: 60px;')

btn2 = QPushButton('Oto Butão')
btn2.setStyleSheet('font-size: 30px;')

btn3 = QPushButton('Mais um Butão')
btn3.setStyleSheet('font-size: 30px;')

layout.addWidget(btn, 1, 1)
layout.addWidget(btn2, 1, 2)
layout.addWidget(btn3, 2, 1, 1, 2)

window.show()
app.exec()
