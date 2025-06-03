from BaseQT import *
from typing import cast

class KeymapList(GridLayout):
    def __init__(self):
        super().__init__()
        self.row_count: int = 0
        self.is_editing = False
    def enable_edit_mode(self):
        self.is_editing = True
        for row_index in range(self.row_count):
            from_wrapper = cast(EditViewWrapper, self.qlayout.itemAt(row_index*4+1).widget())
            to_wrapper = cast(EditViewWrapper, self.qlayout.itemAt(row_index*4+2).widget())
            delete_button = cast(TextButton, self.qlayout.itemAt(row_index*4+3).widget())
            from_wrapper.editing = True
            to_wrapper.editing = True
            delete_button.setVisible(True)
    def disable_edit_mode(self):
        self.is_editing = False
        for row_index in range(self.row_count):
            from_wrapper = cast(EditViewWrapper, self.qlayout.itemAt(row_index*4+1).widget())
            to_wrapper = cast(EditViewWrapper, self.qlayout.itemAt(row_index*4+2).widget())
            delete_button = cast(TextButton, self.qlayout.itemAt(row_index*4+3).widget())
            from_wrapper.editing = False
            to_wrapper.editing = False
            delete_button.setVisible(False)
    def add_row(self, from_key: str, to_key: str):
        index_label = TextLabel(str(self.row_count + 1))
        from_label = TextLabel(from_key)
        from_wrapper = EditViewWrapper(from_label, LineEdit())
        to_label = TextLabel(to_key)
        to_wrapper = EditViewWrapper(to_label, LineEdit())
        delete_button = TextButton(" X ")
        self.add_widgets(
            (index_label, self.row_count, 0),
            (from_wrapper, self.row_count, 1),
            (to_wrapper, self.row_count, 2),
            (delete_button, self.row_count, 3)
        )
        delete_button.clicked.connect(self._on_delete_clicked)
        self.row_count += 1
        delete_button.setVisible(self.is_editing)
        from_wrapper.editing = self.is_editing
        to_wrapper.editing = self.is_editing
    def _remove_row(self, row_index: int):
        if self.row_count == 0: return
        if row_index >= self.row_count:
            raise IndexError(f"Row index {row_index} is equal or greater than row count {self.row_count}")
        index_item = cast(TextLabel, self.qlayout.itemAt(row_index * 4).widget())
        from_wrapper = cast(EditViewWrapper, self.qlayout.itemAt(row_index*4+1).widget())
        to_wrapper = cast(EditViewWrapper, self.qlayout.itemAt(row_index*4+2).widget())
        delete_button = cast(TextButton, self.qlayout.itemAt(row_index*4+3).widget()) 
        widgets: list[QWidget] = [index_item, from_wrapper, to_wrapper, delete_button]
        if any([widget == None for widget in widgets]): 
            raise ValueError(f"Tried to remove null widget at row {row_index}")
        for widget in widgets:
            self.qlayout.removeWidget(widget)
            widget.deleteLater()
        self.row_count -= 1
        for row in range(row_index, self.row_count):
            index_item = cast(TextLabel, self.qlayout.itemAt(row * 4).widget())
            index_item.setText(str(row+1))
    def _clear(self):
        clear_layout(self.qlayout)
        self.row_count = 0
    @Slot()
    def _on_delete_clicked(self):
        sender = cast(TextButton, self.sender())
        row_index = self.qlayout.indexOf(sender) // 4
        self._remove_row(row_index)
        
    def get_data(self) -> list[tuple[str, str]]:
        result: list[tuple[str, str]] = []
        for row_index in range(self.row_count):
            from_wrapper = cast(EditViewWrapper, self.qlayout.itemAt(row_index*4+1).widget())
            to_wrapper = cast(EditViewWrapper, self.qlayout.itemAt(row_index*4+2).widget())
            from_key = cast(TextLabel, from_wrapper._view).text()
            to_key = cast(TextLabel, to_wrapper._view).text()
            result.append((from_key, to_key))
        return result
    def set_data(self, data: list[tuple[str, str]]):
        self._clear()
        for from_key, to_key in data:
            self.add_row(from_key, to_key)