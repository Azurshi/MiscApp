from BaseQT import *
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from qasync import QEventLoop
import asyncio

from .tray import SystemTray
from .window import Window
from data import AppData

class App:
    def __init__(self) -> None:
        self.__app = QApplication(sys.argv)
        self.__tray = SystemTray(QIcon("resources/icon_on.png"), self.__app)
        self.loop = QEventLoop(self.__app)
        asyncio.set_event_loop(self.loop)
    def set_connection(self):
        def hide_window_and_save():
            AppData.save()
            self.__window.hide()
            # self.__app.exit()
        def exit_and_save():
            AppData.save()
            self.__app.exit()
        self.__window.exit_clicked.connect(hide_window_and_save)
        self.__tray.close_selected.connect(hide_window_and_save)
        self.__tray.tray_double_clicked.connect(hide_window_and_save)
        self.__tray.exit_selected.connect(exit_and_save)
        self.__tray.open_selected.connect(lambda: self.__window.show())
        self.__tray.tray_left_clicked.connect(lambda: self.__window.show())
    def setup(self):
        self.__window = Window(None)
    def exec(self):
        self.__window.center_on_screen()
        self.loop.run_forever()