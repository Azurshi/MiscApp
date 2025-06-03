from PySide6.QtWidgets import QWidget, QStackedLayout, QFrame
from typing import Callable, Type, TypeVar, Any
from ..items import *
from ..core import *

TEditWidget = TypeVar("TEditWidget", bound=QWidget)
TViewWidget = TypeVar("TViewWidget", bound=QWidget)

def text_switch_function(edit: LineEdit, view: TextLabel):
    edit.setText(view.text())
def text_finish_function(edit: LineEdit, view: TextLabel):
    view.setText(edit.text())
    edit.setText("")

def combobox_switch_function(edit: ComboBox, view: TextLabel):
    edit.setCurrentText(view.text())
def combobox_finish_function(edit: ComboBox, view: TextLabel):
    view.setText(edit.currentText())
    
class EditViewWrapper(QWidget):
    PredefinedFunctions: dict[tuple[type, type], tuple[Callable[[Any, Any], None], Callable[[Any, Any], None]]] = {
        (LineEdit, TextLabel): (text_switch_function, text_finish_function),
        (LineEdit, TextButton): (text_switch_function, text_finish_function),
        (ComboBox, TextLabel): (combobox_switch_function, combobox_finish_function),
        (ComboBox, TextButton): (combobox_switch_function, combobox_finish_function),
        (TextEdit, TextLabel): (text_switch_function, text_finish_function),
        (TextEdit, TextButton): (text_switch_function, text_finish_function)
    }
    @property
    def editing(self): return self.__editing
    @editing.setter
    def editing(self, value: bool): 
        if self.__editing != value:
            self.__editing = value
            if value == True:
                self.__layout.setCurrentWidget(self._edit)
                if self.switch_func:
                    self.switch_func(self._edit, self._view)
            else:
                self.__layout.setCurrentWidget(self._view)
                if self.finish_func:
                    self.finish_func(self._edit, self._view)
    def __init__(self, 
                 view_widget: TViewWidget,
                 edit_widget: TEditWidget,
                 auto_detect: bool = True,
                 switch_func: Callable[[TEditWidget, TViewWidget], None] | None = None,
                 finish_func: Callable[[TEditWidget, TViewWidget], None] | None = None
        ):
        super().__init__(None)
        self.__editing = False
        self.__layout = QStackedLayout()
        self._view = view_widget
        self._edit = edit_widget
        self.setLayout(self.__layout)
        self.__layout.addWidget(self._view)
        self.__layout.addWidget(self._edit)
        self._view.setParent(self)
        self._edit.setParent(self)
        self.switch_func = switch_func
        self.finish_func = finish_func
        type_tuple = (type(edit_widget), type(view_widget))
        if auto_detect and type_tuple in self.PredefinedFunctions:
            funcs = self.PredefinedFunctions[type_tuple]
            if not self.switch_func: self.switch_func = funcs[0]
            if not self.finish_func: self.finish_func = funcs[1]
            
        