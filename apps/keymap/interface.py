from BaseQT import *
from .collection import KeymapList

class KeymapInterface(ListLayout):
    key_applied = Signal()
    key_canceled = Signal()
    def __init__(self, orientation: Qt.Orientation = Qt.Orientation.Vertical):
        super().__init__(orientation)
        self.set_widget()
        self.set_connection()
        self.set_style()
    def set_widget(self):
        self.status_label = TextLabel()
        self.expand_button = TextButton("Show")
        self.padding_widget = QWidget()
        
        self.button_layout = ListLayout(Qt.Orientation.Horizontal)
        
        self.edit_button = TextButton("Edit")
        self.apply_button = TextButton("Apply")
        self.cancel_button = TextButton("Cancel")
        self.add_button = TextButton(" + New")
        
        self.button_layout.add_widgets(
            self.edit_button, self.apply_button, self.cancel_button, self.add_button
        )
        
        self.key_list_layout = ListLayout(Qt.Orientation.Vertical)
        self.key_list = KeymapList()
        self.key_list_padding = QWidget()
        self.key_list_layout_scroller = ScrollWrapper(self.key_list_layout, Qt.Orientation.Vertical)

        self.key_list_layout.add_widgets(
            self.key_list, (self.key_list_padding, 1)
        )
                
        self.add_widgets(
            self.status_label, self.expand_button, self.button_layout, (self.key_list_layout_scroller, 1), (self.padding_widget, 1)
        )
        
        
    def set_connection(self):
        self.expand_button.clicked.connect(self.__expand_buton_clicked)
        self.edit_button.clicked.connect(self.start_edit_mode)
        self.apply_button.clicked.connect(self.apply_edit_mode)
        self.cancel_button.clicked.connect(self.cancel_edit_mode)
        self.add_button.clicked.connect(lambda: self.key_list.add_row("From key", "To Key"))
    def set_style(self):
        widgets: list[QWidget] = [self.expand_button, self.button_layout]
        for widget in widgets:
            widget.setMinimumHeight(20)
        self.hide_key_list()
        self.edit_button.show()
        self.apply_button.hide()
        self.cancel_button.hide()
        self.add_button.hide()
    @Slot()
    def start_edit_mode(self):
        self.key_list.enable_edit_mode()
        self.edit_button.hide()
        self.apply_button.show()
        self.cancel_button.show()
        self.add_button.show()
    @Slot()
    def apply_edit_mode(self):
        self.key_list.disable_edit_mode()
        self.edit_button.show()
        self.apply_button.hide()
        self.cancel_button.hide()
        self.add_button.hide()
        self.key_applied.emit()
    @Slot()
    def cancel_edit_mode(self):
        self.key_list.disable_edit_mode()
        self.edit_button.show()
        self.apply_button.hide()
        self.cancel_button.hide()
        self.add_button.hide()
        self.key_canceled.emit()
    def show_key_list(self):
        self.expand_button.setText("Hide")
        self.key_list_layout.show()
        self.button_layout.show()
        self.padding_widget.hide()
    def hide_key_list(self):
        self.expand_button.setText("Show")
        self.key_list_layout.hide()
        self.button_layout.hide()
        self.padding_widget.show()
    @Slot()
    def __expand_buton_clicked(self):
        if self.key_list_layout.isVisible():
            self.hide_key_list()
        else:
            self.show_key_list()