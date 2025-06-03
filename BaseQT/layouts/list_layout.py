from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFrame
from typing import cast

class ListLayout(QFrame):
    @property
    def qlayout(self) -> QVBoxLayout | QHBoxLayout:
        return cast(QVBoxLayout | QHBoxLayout, self.layout())
    def __init__(self, orientation: Qt.Orientation = Qt.Orientation.Vertical):
        super().__init__(None)
        if orientation == Qt.Orientation.Vertical:
            self.setLayout(QVBoxLayout())
        else:
            self.setLayout(QHBoxLayout())
        self.qlayout.setSpacing(0)
        self.qlayout.setContentsMargins(0,0,0,0)
    def add_widget(self, arg__1: QWidget, stretch: int | None = None, alignment: Qt.AlignmentFlag | None = None):
        arg__1.setParent(self)
        if alignment and stretch:
            self.qlayout.addWidget(arg__1, stretch, alignment)
        elif stretch:
            self.qlayout.addWidget(arg__1, stretch)
        elif alignment:
            self.qlayout.addWidget(arg__1, alignment=alignment)
        else:
            self.qlayout.addWidget(arg__1)
    def add_widgets(self, *widgets: QWidget | tuple[QWidget, int] | tuple[QWidget, int, Qt.AlignmentFlag]):
        for widget in widgets:
            if isinstance(widget, QWidget):
                self.add_widget(widget)
            else:
                self.add_widget(*widget) #type:ignore
