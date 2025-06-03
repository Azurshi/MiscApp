from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QStackedLayout
from typing import cast
class MainWindow(QMainWindow):
    @property
    def qlayout(self) -> QStackedLayout:
        return cast(QStackedLayout, self.central_widget.layout())
    def __init__(self, parent: QWidget | None, flags: Qt.WindowType = Qt.WindowType.Window):
        super().__init__(parent, flags)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.centralWidget().setLayout(QStackedLayout())
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
