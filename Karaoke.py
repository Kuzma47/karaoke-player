import threading
import time
from datetime import timedelta

from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

from config import *


def init_line(line: QLabel):
    line.setTextFormat(Qt.RichText)
    line.setStyleSheet(f"color: {KARAOKE_TEXT_COLOR}")
    line.setMaximumHeight(100)
    line.setAlignment(Qt.AlignCenter)
    line.setFont(QFont(KARAOKE_TEXT_FONT, 50))
    return line


class Karaoke(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.text_thread = threading.Thread(target=self.run_text)
        self.path = None
        self.stop_flag = False
        self.parent = parent
        self.line, self.word = 0, 0
        self.text = []

        self.layout = QVBoxLayout()
        self.karaoke_player = QMediaPlayer()

        self.pic = QWidget()
        self.pic.setMinimumHeight(600)
        self.pic.setMaximumHeight(600)
        self.layout.addWidget(self.pic)

        self.lines = list(map(init_line, [QLabel(), QLabel()]))
        self.layout.addWidget(self.lines[0])
        self.layout.addWidget(self.lines[1])

        self.setLayout(self.layout)

    def start_karaoke(self, path):
        song = QMediaContent(QUrl.fromLocalFile(path + "audio.mp3"))
        self.karaoke_player.setMedia(song)
        self.path = path

        self.pic.setStyleSheet(  # f"background-repeat: no-repeat;"
                               f"background-position: center;"
                               f"background-image: url({path}/back.jpg);"
                               )

        self.load_text(path)
        for i in range(2):
            self.lines[i].setText(self.get_line(i))

        self.karaoke_player.play()
        self.text_thread.start()

    def stop_karaoke(self):
        self.stop_flag = True

    def load_text(self, path):
        self.text = []
        song_text = open(f'{path}text.txt', encoding="utf-8").readlines()
        for line in song_text:
            self.text += [[[
                word.split(':')[0],
                timedelta(milliseconds=int(
                    float(word.split(':')[1]) * 1000))]
                             for word in line.split(';')[:-1]]]

    def get_line(self, index):
        if index != self.line:
            return " ".join([word[0] for word in self.text[index]])

        pos = self.word + 1
        old_words = ''.join([w[0] for w in self.text[self.line][:pos]])
        new_words = ''.join([w[0] for w in self.text[self.line][pos:]])

        return f'<p><span style="color: {BUTTON_TEXT_COLOR};">' \
               f'{old_words}</span>{new_words}</p>'

    def run_text(self):
        while not self.stop_flag:
            if self.word == len(self.text[self.line]):
                self.word = 0
                self.line += 1

                self.lines[(self.line - 1) % 2].setText(
                    '' if self.line >= len(self.text) - 1
                    else self.get_line(self.line + 1))

                if self.line == len(self.text):
                    return

            line = self.lines[self.line % 2]
            text = self.get_line(self.line)
            line.setText(text)
            time.sleep(
                self.text[self.line][self.word][1].total_seconds())
            self.word += 1
