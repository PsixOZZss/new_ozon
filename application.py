from subprocess import Popen
import asyncio
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QDialog
import sys
import os
import threading
from Bot import app_



class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Cum')
        self.setGeometry(300, 250, 350, 200)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        self.btn_start = QtWidgets.QPushButton(self)
        self.btn_start.move(70, 120)
        self.btn_start.setText('Run bot')
        self.btn_start.adjustSize()
        self.btn_start.clicked.connect(self.thread_start)

    # @staticmethod
    def start_script(self):
        token = self.textbox.text()
        app_(token)

    @staticmethod
    def callback(self):
        event_loop_a = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop_a)
        asyncio.get_event_loop().call_soon(self.start_script())
        event_loop_a.run_forever()

    def thread_start(self):
        ts = threading.Thread(target=self.callback, daemon=True, args=[self])
        ts.start()


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    application()



# def hello(thread_name):
#     print('hello from thread {}!'.format(thread_name))

# event_loop_a = asyncio.new_event_loop()

# def callback_a():
#     asyncio.set_event_loop(event_loop_a)
#     asyncio.get_event_loop().call_soon(lambda: self.start_script())
#     event_loop_a.run_forever()

# thread_a = Thread(target=callback_a, daemon=True)
# thread_a.start()