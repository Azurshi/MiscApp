from PySide6.QtCore import Qt
from BaseQT import *
from .sliders import *

class SliderList(GridLayout):
    def __init__(self):
        super().__init__()
        self.set_widget()
    def set_widget(self):
        self.color_brightness_slider = ColorBrightnessSlider()
        self.color_brightness_title = TextLabel(self.color_brightness_slider.name)
        self.color_brightness_reset = TextButton("Reset")
        self.color_brightness_reset.clicked.connect(self.color_brightness_slider.reset)
        
        self.application_brightness_slider = ApplicationBrightnessSlider()
        self.application_brightness_title = TextLabel(self.application_brightness_slider.name)
        self.application_brightness_reset = TextButton("Reset")
        self.application_brightness_reset.clicked.connect(self.application_brightness_slider.reset)
        
        self.display_brightness_slider = DisplayBrightnessSlider()
        self.display_brightness_title = TextLabel(self.display_brightness_slider.name)
        self.display_brightness_reset = TextButton("Reset")
        self.display_brightness_reset.clicked.connect(self.display_brightness_slider.reset)
        self.add_widgets(
            (self.color_brightness_title, 0, 0), (self.color_brightness_slider, 0, 1), (self.color_brightness_reset, 0, 2),
            (self.application_brightness_title, 1, 0), (self.application_brightness_slider, 1, 1), (self.application_brightness_reset, 1, 2),
            (self.display_brightness_title, 2, 0), (self.display_brightness_slider, 2, 1), (self.display_brightness_reset, 2, 2)
        )
        
        self.qlayout.setColumnStretch(1, 1)
    