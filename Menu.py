from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QVBoxLayout,\
    QWidget, QHBoxLayout, QScrollArea

from config import MAIN_TEXT_COLOR


def create_title_button(text):
    button = QPushButton(text)
    button.setStyleSheet("border: 0;"
                         f"color: {MAIN_TEXT_COLOR};"
                         "height: 100px;"
                         "margin: 0px 0px 0px 0px;"
                         "font-size: 80px;")
    return button


class Menu(QWidget):
    def __init__(self, title=None, parent=None):
        super(Menu, self).__init__(parent)
        self.outer_layout = QVBoxLayout()

        self.upper_layout = QHBoxLayout()
        self.outer_layout.addLayout(self.upper_layout)
        self.upper_layout.addWidget(create_title_button(title))
        self.upper_layout.setAlignment(Qt.AlignLeft)

        self.buttons = QWidget()
        self.buttons_layout = QVBoxLayout()
        self.buttons_layout.setAlignment(Qt.AlignLeft)
        self.buttons_layout.setSpacing(50)

        self.buttons.setLayout(self.buttons_layout)
        self.buttons.setFixedWidth(1000)

        meny_layout = QHBoxLayout()
        scroll = QScrollArea()
        scroll.setStyleSheet("border: 0;")
        scroll.setWidget(self.buttons)
        scroll.setWidgetResizable(True)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        meny_layout.addWidget(scroll)

        self.outer_layout.addLayout(meny_layout)

        self.setLayout(self.outer_layout)

    def add_menu_button(self, widget: QPushButton):
        self.buttons_layout.addWidget(widget)

    def add_upper_menu_button(self, widget):
        self.upper_layout.addWidget(widget)
