from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QWidget, QCheckBox
from typing import Callable
from ..core import *

class CheckBox(QCheckBox):
    def __init__(self, text: str = ""):
        super().__init__(text, None)
class KeyCheckBox(CheckBox, IKeyView):
    key_check_state_changed = Signal(str, Qt.CheckState)
    def __init__(self, text = "", get_value_func: Callable[[str], str] | None = None):
        super().__init__(text)
        if get_value_func != None:
            self._get_value_func = get_value_func
        self.checkStateChanged.connect(self.__on_check_state_changed)
    def set_value(self, value):
        self.setText(value or "")
    @Slot(Qt.CheckState)
    def __on_check_state_changed(self, state: Qt.CheckState):
        self.key_check_state_changed.emit(self.key, state)