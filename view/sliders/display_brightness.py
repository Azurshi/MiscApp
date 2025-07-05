from BaseQT import *
from .interface import ISlider
from brightness import DisplayBrightness

class DisplayBrightnessSlider(Slider, ISlider[float]):
    def __init__(self, orientation: Qt.Orientation = Qt.Orientation.Horizontal):
        Slider.__init__(self, orientation)
        ISlider[float].setup(self, "display_brightness", "Display Brightness", 0, 1)
        self.setup()
    def setup(self):
        self.setMinimum(0)
        self.setMaximum(1000)
        self.setSingleStep(1)
        
        self.valueChanged.connect(self._on_value_changed)
        
        self.setValue(int(DisplayBrightness.get_current_brightness() * 1000))
    @Slot()
    def reset(self):
        value = 1
        self.setValue(value * 1000)
        DisplayBrightness.set_brightness(value)
    @Slot(int)
    def _on_value_changed(self, value: int):
        percent = float(value) / 1000
        DisplayBrightness.set_brightness(percent)