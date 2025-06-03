from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QComboBox
from typing import Callable
from ..core import *

class ComboBox(QComboBox):
    def __init__(self, items: list[str] | tuple[str, ...] = []):
        super().__init__(None)
        self.addItems(items)
class KeyComboBox(ComboBox, IKeysView):
    def __init__(self, items: list[str] = [], get_value_func: Callable[[str], str] | None = None):
        super().__init__(items)
        if get_value_func != None:
            self._get_value_func = get_value_func
    def set_value(self, values: list[str]):
        self.clear()
        self.addItems(values) 
    def set_current_key(self, key: str | None):
        if key != None:
            self.setCurrentText(self._get_value_func(key))
        else:
            self.setCurrentIndex(len(self._keys)-1)
    def get_current_key(self):
        return self._keys[self.currentIndex()]