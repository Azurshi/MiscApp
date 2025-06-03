from BaseQT import *

class BrightnessInterface(ListLayout):
    def __init__(self, orientation: Qt.Orientation = Qt.Orientation.Vertical):
        super().__init__(orientation)
        self.set_widget()
        self.set_connection()
        self.set_style()
    def set_widget(self):
        self.main_layout = GridLayout()
        self.add_widget(self.main_layout)
        self.brightness_slider = Slider(Qt.Orientation.Horizontal)
        self.factor_slider = Slider(Qt.Orientation.Horizontal)
        self.brightness_reset_button = TextButton("Reset")
        self.factor_reset_button = TextButton("Reset")
        self.main_layout.add_widgets(
            (TextLabel("Brightness"), 0, 0), (self.brightness_slider, 0, 1), (self.brightness_reset_button, 0, 2),
            (TextLabel("Factor"), 1, 0), (self.factor_slider, 1, 1), (self.factor_reset_button, 1, 2),
            (QWidget(), 2, 0)
        )
        self.main_layout.qlayout.setColumnStretch(1, 1)
        self.main_layout.qlayout.setRowStretch(2, 1)
    def set_connection(self):
        pass
    def set_style(self):
        style = Style()
        style.padding = 2
        style.apply(self.brightness_reset_button)
        style.apply(self.factor_reset_button)
