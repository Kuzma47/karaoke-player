import os

from PyQt5.QtWidgets import QMainWindow, QPushButton, QStackedWidget

from Karaoke import Karaoke
from Menu import Menu
from config import *


def create_upper_menu_button(text):
    button = QPushButton(text)
    button.setStyleSheet(f"background-color: {BUTTON_COLOR};"
                         "height: 150px;"
                         "font-size: 50px;")
    return button


def create_menu_button(text):
    button = QPushButton(text)
    button.setFixedHeight(150)
    button.setFixedWidth(1470)
    button.setStyleSheet(f"color: {BUTTON_TEXT_COLOR};"
                         f"background-color: {BUTTON_COLOR};"
                         "height: 150px;"
                         "font-size: 50px;")
    return button


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("Karaoke")
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.set_color()
        self.create_main_menu()
        self.karaoke = Karaoke(self)

    def set_color(self):
        self.setStyleSheet(f"color: {BUTTON_TEXT_COLOR};"
                           f"background-color: {BACKGROUND_COLOR};")

    def change_widget(self, widget):
        self.central_widget.addWidget(widget)
        self.central_widget.setCurrentWidget(widget)

    def create_main_menu(self):
        menu = Menu("Выберите исполнителя", self)
        for performer in os.listdir("data"):
            button = create_menu_button(performer)
            button.clicked.connect(lambda _, p=performer:
                                   self.create_audios_menu(p))
            menu.add_menu_button(button)
        self.change_widget(menu)

    def create_audios_menu(self, performer):
        menu = Menu("Выберите композицию", self)
        back_button = create_upper_menu_button("Назад")
        back_button.setFixedWidth(300)
        back_button.setFixedHeight(70)
        back_button.clicked.connect(lambda: self.create_main_menu())
        menu.add_upper_menu_button(back_button)
        for audio in os.listdir(f"data/{performer}"):
            button = create_menu_button(audio)
            button.\
                clicked.connect(lambda _, p=f"data/{performer}/{audio}/":
                                            self.open_karaoke(p))
            menu.add_menu_button(button)
        self.change_widget(menu)

    def open_karaoke(self, path):
        self.karaoke.start_karaoke(path)
        self.change_widget(self.karaoke)
