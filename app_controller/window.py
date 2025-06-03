from BaseQT import *

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QColor, QCloseEvent
from typing import Union, Type, cast

from core import *

class Window(MainWindow):
    exit_clicked = Signal()
    def __init__(self, parent: QWidget | None, flags: Qt.WindowType = Qt.WindowType.Window):
        super().__init__(parent, flags)
        self.set_widget()
        self.set_connection()
        self.set_style()
        self.buttons_map: dict[TextButton, Type[IApp]] = {}
    def __cleanup(self):
        layout = self.__app_layout.qlayout
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
                print(f"{type(widget)} deleted")
            elif item.layout():
                clear_layout(item.layout())
    @Slot()
    def __on_app_button_clicked(self):
        self.__cleanup()
        sender = cast(TextButton, self.sender())
        app_type = self.buttons_map[sender]
        self.__app_layout.add_widget(app_type.get_foreground_interface())
        print(app_type().app_name)
    def register_app(self, app_type: Type[IApp]):
        button = TextButton(app_type.app_name)
        self.__buttons_layout.add_widget(button)
        button.clicked.connect(self.__on_app_button_clicked)
        self.buttons_map[button] = app_type
        app_type.start_background_process()
    def set_widget(self):
        self.__main_layout = ListLayout(Qt.Orientation.Vertical)
        self.__buttons_layout = ListLayout(Qt.Orientation.Horizontal)
        self.__app_layout = StackLayout()
        self.add_widget(self.__main_layout)
        self.__main_layout.add_widget(self.__buttons_layout)
        self.__main_layout.add_widget(self.__app_layout, 1)
    def set_connection(self):
        style = Style()
        style.background_color = "blue"
        style.apply(self.__buttons_layout)
    def set_style(self):
        self.show()
        self.__buttons_layout.setMinimumHeight(20)
    def center_on_screen(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(screen_geometry.x() + x, screen_geometry.y() + y)
    def closeEvent(self, event: QCloseEvent):
        event.ignore()
        self.exit_clicked.emit()