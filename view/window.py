from BaseQT import *

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QColor, QCloseEvent
from typing import Union, Type, cast
from .slider_list import SliderList
from data import AppData

class Window(MainWindow):
    exit_clicked = Signal()
    def __init__(self, parent: QWidget | None, flags: Qt.WindowType = Qt.WindowType.Window):
        super().__init__(parent, flags)
        self.setWindowTitle("Brightness App")
        self.set_widget()
        self.set_connection()
        self.set_style()
        AppData.app_hwnd = self.winId()
    def set_widget(self):
        self.__main_layout = SliderList()
        self.__app_layout = StackLayout()
        self.add_widget(self.__main_layout)
        self.__main_layout.add_widget(self.__app_layout, 1)
    def set_connection(self):
        style = Style()
        style.background_color = "blue"
    def set_style(self):
        self.show()
    def center_on_screen(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(screen_geometry.x() + x, screen_geometry.y() + y)
    def closeEvent(self, event: QCloseEvent):
        event.ignore()
        self.exit_clicked.emit()