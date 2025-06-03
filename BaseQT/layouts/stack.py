from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QStackedLayout, QFrame
from typing import cast

class StackLayout(QFrame):
    @property
    def qlayout(self) -> QStackedLayout:
        return cast(QStackedLayout, self.layout())
    def __init__(self):
        super().__init__(None)
        self.setLayout(QStackedLayout())
        self.qlayout.setSpacing(0)
        self.qlayout.setContentsMargins(0,0,0,0)
    def add_widget(self, arg__1: QWidget):
        arg__1.setParent(self)
        self.qlayout.addWidget(arg__1)
    def add_widgets(self, *widgets: QWidget):
        for widget in widgets:
            self.add_widget(widget)
    def set_current(self, widget: QWidget):
        self.qlayout.setCurrentWidget(widget)
