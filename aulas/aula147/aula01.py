"""`QApplication` e Q`PushButton` de `PySide6.QtWidgets`"""
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão

from PySide6.QtWidgets import QApplication, QPushButton  # type: ignore
import sys

app = QApplication(sys.argv)

btn = QPushButton('Butão')
btn.setStyleSheet('font-size: 60px; color: red;')
btn.show()

btn2 = QPushButton('Oto Butão')
btn2.show()

app.exec()
