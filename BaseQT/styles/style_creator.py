from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import QWidget, QMainWindow
from typing import Literal, Callable, Any, Type
class Convertor:
    @classmethod
    def QColor(cls, input : QColor | str | tuple[int, int, int] | tuple[int, int, int, int] | int) -> str | None:
        if isinstance(input, QColor):
            return f"rgb({input.red()}, {input.green()}, {input.blue()})"
        elif isinstance(input, str):
            if input[0] == "#":
                input = input[1:]
                if len(input) == 6:
                    r, g, b = tuple(int(input[i:i+2], 16) for i in (0, 2, 4))
                    return f"rgb({r}, {g}, {b})"
                elif len(input) == 8:
                    r, g, b, a = tuple(int(input[i:i+2], 16) for i in (0, 2, 4, 6))
                    return f"rgba({r}, {g}, {b}, {a})"
                else:
                    print(f"Invalid color format {input}")
                    return None
            else:
                return input
        elif isinstance(input, tuple):
            if len(input) == 3:
                r, g, b = input
                return f"rgb({r}, {g}, {b})"
            elif len(input) == 4:
                r, g, b, a = input
                return f"rgba({r}, {g}, {b}, {a})"
            else:
                print(f"Invalid color format {input}")
                return None
        elif isinstance(input, int):
            r = (input >> 24) & 0xFF 
            g = (input >> 16) & 0xFF
            b = (input >> 8) & 0xFF
            a = input & 0xFF
            return f"rgba({r}, {g}, {b}, {a})"
        else:
            print(f"Invalid color format {input}")
            return None
class Style:
    @property
    def size(self):
        return (self.width, self.height)
    @size.setter
    def size(self, value: tuple[int, int]):
        self.width, self.height = value
    @property
    def max_size(self):
        return (self.max_width, self.max_height)
    @max_size.setter
    def max_size(self, value: tuple[int, int]):
        self.max_width, self.max_height = value
    @property
    def min_size(self):
        return (self.min_width, self.min_height)
    @min_size.setter
    def min_size(self, value: tuple[int, int]):
        self.min_width, self.min_height = value
    @property
    def padding(self):
        return (self.padding_top, self.padding_right, self.padding_bottom, self.padding_left)
    @padding.setter
    def padding(self, value: int | tuple[int, int] | tuple[int, int, int, int] | None):
        if not value or isinstance(value, int):
            self.padding_top = value
            self.padding_right = value
            self.padding_bottom = value
            self.padding_left = value
        elif isinstance(value, tuple) and len(value) == 2:
            self.padding_top, self.padding_left = value
            self.padding_bottom, self.padding_right = value
        elif isinstance(value, tuple) and len(value) == 4:
            self.padding_top, self.padding_right, self.padding_bottom, self.padding_left = value
    @property
    def margin(self):
        return (self.margin_top, self.margin_right, self.margin_bottom, self.margin_left)
    @margin.setter
    def margin(self, value: int | tuple[int, int] | tuple[int, int, int, int] | None):
        if not value or isinstance(value, int):
            self.margin_top = value
            self.margin_right = value
            self.margin_bottom = value
            self.margin_left = value
        elif isinstance(value, tuple) and len(value) == 2:
            self.margin_top, self.margin_left = value
            self.margin_bottom, self.margin_right = value
        elif isinstance(value, tuple) and len(value) == 4:
            self.margin_top, self.margin_right, self.margin_bottom, self.margin_left = value
    @property
    def border(self):
        return (self.border_width, self.border_style, self.border_color, self.border_radius)
    @border.setter
    def border(self, value: tuple[int, Literal["solid"], QColor | str] | tuple[int, Literal["solid"], QColor | str, int] | None):
        if not value:
            self.border_width = value
            self.border_style = value
            self.border_color = value
            self.border_radius
        elif isinstance(value, tuple) and len(value) == 3:
            self.border_width, self.border_style, self.border_color = value
        elif isinstance(value, tuple) and len(value) == 4:
            self.border_width, self.border_style, self.border_color, self.border_radius = value
        
    @property
    def size_unit(self):
        return self._size_unit
    @size_unit.setter
    def size_unit(self, value: Literal["px", "em"]):
        self._size_unit = value
    def __init__(self):
        self.state: Literal[None ,"hover", "pressed", "checked", "unchecked", "enabled", "disabled", "focus", "interminate", "read-only", "active", "first", "last", "middle",
                        "QPushButton:menu-indicator", "QPushButton:deault",
                        "QComboBox:drop-down", "QComboBox:drop-arrow",
                        "QScrollBar:handle", "QScrollBar:add-line", "QScrollBar:sub-line",
                        "QMenu:seperator",
                        "QTabBar:tab", "QTabBar:pane",
                        "QHeaderView:section", "QTableWidget:item",
                        "QSlider:groove", "QSlider:handle",
                        "QProgressBar:chunk",
                        "QToolTip:???",
                        "QFrame:box", "QFrame:shadow", None] = None
        self.background : Literal["solid", "qlineargradient?", "qradialgradient?", "qconicalgradient?", None] = None
        self.background_color : QColor | str | None = None
        self.color : QColor | str | None = None
        self.font : QFont | None = None
        self.font_family : str | None = None
        self.font_size : int | str | None = None
        self.font_weight : int | str | None = None
        self.font_style : str | None = None
        self.padding_top : int | None = None
        self.padding_bottom : int | None = None
        self.padding_left : int | None = None
        self.padding_right : int | None = None
        self.margin_top : int | None = None
        self.margin_bottom : int | None = None
        self.margin_left : int | None = None
        self.margin_right : int | None = None
        self.border_style : str | None = None
        self.border_width : int | None = None
        self.border_color : QColor | str | None = None
        self.border_radius : int | None = None
        self.min_width : int | None = None
        self.min_height : int | None = None
        self.max_width : int | None = None
        self.max_height : int | None = None
        self.width : int | None = None
        self.height : int | None = None
        self.text_align : Literal["center", "left", "right", None] = None
        self.image : str | None = None
        self.background_image : str | None = None
        self.selection_color : QColor | str | None = None
        self.selection_background_color : QColor | str | None = None
        self.spacing : int | None = None
        self.line_height : int | None = None
        self.opacity : float | None = None
        self.outline : str | None = None
        self.border_image : str | None = None
        self.qproperty_alignment : str | None = None
        self.qproperty_iconSize : str | None = None
        self.qproperty_text : str | None = None
        self.qproperty_cursor : str | None = None
        self.qproperty_icon : str | None = None
        self.qlineargradient : str | None = None
        self.qradialgradient : str | None = None 
        self.qconicalgradient : str | None = None
        self._size_unit : Literal["px", "em"] = "px"

    def __evaluate(self) -> str:
        process_function : dict[str, Callable[[Any], str | None]] = {
            # "background" : background,
            "background_color" : Convertor.QColor,
            "color" : Convertor.QColor,
            "font" : lambda i : None if isinstance(i, QFont) else i,
            # "font-family" : font_family,
            # "font-size" : None,
            # "font-weight" : font_weight,
            # "font-style" : font_style,

            # "border" : border,
            # "border-style" : border_style,
            "border-color" : Convertor.QColor,
            # "image" : image,
            # "background-image" : background_image,
            "selection-color" :  Convertor.QColor,
            "selection-background-color" : Convertor.QColor,
            # "opacity" : opacity,
            # "outline" : outline,
            # "border-image" : border_image
        }
        result: list[str] = []
        for field_name, field_value in self.__dict__.items():
            if field_value != None and field_name[0] != '_':
                if field_name in process_function:
                    field_value = str(process_function[field_name](field_value))
                field_name = field_name.replace("_", "-")
                line = field_name + ": " + str(field_value)
                if isinstance(field_value, int):
                    line += self._size_unit
                result.append(line)
        return ";".join(result)
    def apply(self, target : QWidget):
        state = ""
        if (self.state != None):
            state.replace(":", "::")
            state = ":" + self.state
        if (self.font and isinstance(self.font, QFont)):
            target.setFont(self.font)
        style_sheet = target.__class__.__name__ + state + "{" + self.__evaluate() + "}"
        # print(style_sheet)
        target.setStyleSheet(style_sheet)
        #Specific
        if isinstance(target, QMainWindow):
            if self.size != (None, None):
                target.resize(self.width or 0, self.height or 0)
        
        return style_sheet
    def apply_batch(self, *targets: QWidget):
        for target in targets:
            self.apply(target)
    def evaluate(self, target_classes: Type[QWidget] | list[type[QWidget]] | None = None):
        if target_classes == None: return self.evaluate([QWidget])
        state = ""
        if (self.state != None):
            state.replace(":", "::")
            state = ":" + self.state
        if isinstance(target_classes, Type):
            prefix = target_classes.__name__ + state
        else:
            prefix = ",".join([target_class.__name__ + state for target_class in target_classes])
        style_sheet = prefix + "{" + self.__evaluate() + "}"
        return style_sheet
    def evaluate_with_name(self, target_class: type[QWidget], object_name: str):
        state = ""
        if (self.state != None):
            state.replace(":", "::")
            state = ":" + self.state
        prefix = f"{target_class.__name__}#{object_name}{state}"
        style_sheet = prefix + " {" + self.__evaluate() + "}"
        return style_sheet
