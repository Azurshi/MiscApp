from PySide6.QtWidgets import QLayout

def clear_layout(layout: QLayout, retain_num: int = 0):
    while layout.count() > retain_num:
        item = layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()
        elif item.layout():
            clear_layout(item.layout())