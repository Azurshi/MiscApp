from PySide6.QtCore import Qt
from brightness import ColorBrightness
from BaseQT import *
from .interface import ISlider
from data import AppData

class ColorBrightnessSlider(Slider, ISlider[float]):
    def __init__(self, orientation: Qt.Orientation = Qt.Orientation.Horizontal):
        Slider.__init__(self, orientation)
        ISlider[float].setup(self, "color_brightness", "Color Brightness", 0, 1)
        self.setup()
    def setup(self):
        self.setMinimum(0)
        self.setMaximum(1000)
        self.setSingleStep(1)
        
        self.valueChanged.connect(self._on_value_changed)
        
        self.setValue(int(AppData.color_brightness * 1000))
        ColorBrightness.set_brightness(AppData.color_brightness)
    @Slot()
    def reset(self):
        value = AppData.get_default("color_brightness")
        self.setValue(value * 1000)
        ColorBrightness.set_brightness(value)
        AppData.color_brightness = value
    @Slot(int)
    def _on_value_changed(self, value: int):
        AppData.color_brightness = float(value) / 1000
        ColorBrightness.set_brightness(AppData.color_brightness)