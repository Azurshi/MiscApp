from ..core import *
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QSizePolicy, QLineEdit, QTextEdit
from typing import Callable

class TextLabel(QLabel):
    def __init__(self, text: str = ""):
        super().__init__(text, None)
    def set_font_size(self, font_size: int):
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)
class KeyTextLabel(TextLabel, IKeyView):
    def __init__(self, text: str = "", get_value_func: Callable[[str], str] | None = None):
        super().__init__(text)
        if get_value_func != None:
            self._get_value_func = get_value_func
    def set_value(self, value: str | None):
        self.setText(value or "")
class TextButton(QPushButton):
    def __init__(self, text: str = ""):
        super().__init__(text, None)
        self.setMinimumSize(1, 1)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
class KeyTextButton(TextButton, IKeyView):
    key_clicked = Signal(str)
    def __init__(self, text = "", get_value_func: Callable[[str], str] | None = None):
        super().__init__(text)   
        if get_value_func != None:
            self._get_value_func = get_value_func
    @Slot() 
    def _on_clicked(self):
        self.key_clicked.emit(self.key or "")
class LineEdit(QLineEdit):
    focus_outted = Signal()
    enter_pressed = Signal()
    esc_pressed = Signal()
    def __init__(self, text: str = ""):
        super().__init__(text, None)
    def focusOutEvent(self, arg__1):
        self.focus_outted.emit()
        super().focusOutEvent(arg__1)
    def keyPressEvent(self, arg__1):
        if arg__1.key() in (Qt.Key.Key_Enter, Qt.Key.Key_Return):
            self.enter_pressed.emit()
        elif arg__1.key() == Qt.Key.Key_Escape:
            self.esc_pressed.emit()
        super().keyPressEvent(arg__1)
class TextEdit(QTextEdit):
    def __init__(self, text: str = ""):
        super().__init__(text, None)        
    def text(self) -> str:
        return self.toPlainText()
