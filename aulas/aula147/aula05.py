"""Trabalhando com classes e herança no PySide6"""

from PySide6.QtCore import Slot  # type: ignore
from PySide6.QtWidgets import QApplication, QGridLayout, QMainWindow, QPushButton, QWidget   # type: ignore
import sys


class Window(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.central = QWidget()
        self.setCentralWidget(self.central)
        self.setWindowTitle('Bagulho doidão')

        self.menu = self.menuBar()
        self.option = self.menu.addMenu('Opção')
        self.action = self.option.addAction('Ação')
        self.another_action = self.option.addAction('Outra Ação')
        self.another_action.setCheckable(True)

        self.status = self.statusBar()
        self.status.showMessage('Showzão de bola!')

        self.layout = QGridLayout()
        self.central.setLayout(self.layout)

        self.btn = self.add_btn('Butão', 30)
        self.btn2 = self.add_btn('Oto Butão', 30)
        self.btn3 = self.add_btn('Mais um Butão', 60)

        self.layout.addWidget(self.btn, 1, 1)
        self.layout.addWidget(self.btn2, 1, 2)
        self.layout.addWidget(self.btn3, 2, 1, 1, 2)

        self.action.triggered.connect(self.change_status)
        self.another_action.hovered.connect(lambda: print(
            'Marcada!' if self.another_action.isChecked() else 'Desmarcada!'))
        self.another_action.toggled.connect(self.check_action)
        self.btn.clicked.connect(self.check_click)

    def add_btn(self, txt: str, txt_size: int) -> QPushButton:
        btn = QPushButton(txt)
        btn.setStyleSheet(f'font-size: {txt_size}px;')
        return btn

    @Slot()
    def change_status(self) -> None:
        self.status.showMessage('Hello, World!')

    @Slot()
    def check_action(self) -> None:
        print('Ação checada!' if self.another_action.isChecked()
              else 'Ação deschecada!')

    @Slot()
    def check_click(self) -> None:
        print('Botão clicado!')
        self.another_action.setChecked(not self.another_action.isChecked())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
