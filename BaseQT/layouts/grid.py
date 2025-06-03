from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QFrame
from typing import cast

class GridLayout(QFrame):
    @property
    def qlayout(self) -> QGridLayout:
        return cast(QGridLayout, self.layout())
    def __init__(self):
        super().__init__(None)
        self.setLayout(QGridLayout())
        self.qlayout.setSpacing(0)
    def add_widget(self, arg__1: QWidget, row: int = 0, column: int = 0, rowSpan: int = 1, columnSpan: int = 1, alignment: Qt.AlignmentFlag | None = None):
        if alignment:
            self.qlayout.addWidget(arg__1, row, column, rowSpan, columnSpan, alignment)
        else:
            self.qlayout.addWidget(arg__1, row, column, rowSpan, columnSpan)
    def add_widgets(self, *widgets: QWidget | tuple[QWidget, int, int] | tuple[QWidget, int, int, Qt.AlignmentFlag] | tuple[QWidget, int, int, int, int] | tuple[QWidget, int, int, int, int, Qt.AlignmentFlag]):
        for widget in widgets:
            if isinstance(widget, QWidget):
                self.add_widget(widget)
            elif len(widget) == 4:
                self.add_widget(*widget[:3], alignment=widget[3])
            else:
                self.add_widget(*widget) #type:ignore
            
        