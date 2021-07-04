import socket

from os import getlogin

# Работа с изображение
from PIL import Image
import io
import numpy as np
from random import randint
import pyautogui
# Поток
from threading import Thread
# PyQt5
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QPushButton, QAction, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect, Qt


print("[SERVER]: STARTED")
sock = socket.socket()
sock.bind(('172.20.10.5', 9091)) # Your Server
sock.listen()
conn, addr = sock.accept()

class Dekstop(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def ChangeImage(self):
        try:
            print("[SERVER]: CONNECTED: {0}!".format(addr[0]))
            while True:
                img_bytes = conn.recv(9999999)
                self.pixmap.loadFromData(img_bytes)
                self.label.setScaledContents(True)
                self.label.resize(self.width(), self.height())
                self.label.setPixmap(self.pixmap)
        except ConnectionResetError:
            conn.close()

    def initUI(self):
        self.pixmap = QPixmap()
        self.label = QLabel(self)
        self.label.resize(self.width(), self.height())
        self.setGeometry(QRect(pyautogui.size()[0] // 4, pyautogui.size()[1] // 4, 800, 450))
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle("[SERVER]: ")
        self.start = Thread(target=self.ChangeImage, daemon=True)
        self.start.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Dekstop()
    ex.show()
    sys.exit(app.exec())