from BaseQT import *
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon


from core import *
from .window import Window
from .tray import SystemTray

class App:
    def __init__(self) -> None:
        self.__app = QApplication(sys.argv)
        self.__app_data: list[Type[IAppData]] = []
        self.__tray = SystemTray(QIcon("resources/icon_on.png"), self.__app)
    def set_connection(self):
        def hide_window_and_save():
            self.__window.hide()
            self.save_data()
        def exit_and_save():
            self.__app.exit()
            self.save_data()
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
        self.__app.exec()
        self.save_data()
    def save_data(self):
        for app_data in self.__app_data:
            app_data.save()
    def register_app(self, app_type: Type[IApp], app_data_type: Type[IAppData] | None):
        self.__window.register_app(app_type)
        if app_data_type != None:
            self.__app_data.append(app_data_type)