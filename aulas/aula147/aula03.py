"""QMainWindow e centralWidget"""
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec

from PySide6.QtWidgets import QApplication, QGridLayout, QMainWindow, QPushButton, QWidget   # type: ignore
import sys

def change_status(status_bar): 
    status_bar.showMessage('Hello, World!')

app = QApplication(sys.argv)

window = QMainWindow()
central = QWidget()
window.setCentralWidget(central)
window.setWindowTitle('Bagulho doidão')

menu = window.menuBar()
option = menu.addMenu('Opção')
action = option.addAction('Ação')

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

action.triggered.connect(lambda: change_status(status))

window.show()
app.exec()
