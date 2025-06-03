from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QDialog, QStackedLayout
from typing import cast

class Dialog(QDialog):
    @property
    def qlayout(self) -> QStackedLayout:
        return cast(QStackedLayout, self.layout())
    def __init__(self, parent: QWidget, f:  Qt.WindowType = Qt.WindowType.Window):
        super().__init__(parent, f)
        self.setLayout(QStackedLayout())
    def add_widget(self, arg__1: QWidget):
        arg__1.setParent(self)
        self.qlayout.addWidget(arg__1)