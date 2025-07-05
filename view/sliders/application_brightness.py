from BaseQT import *
from .interface import ISlider
from brightness import ApllicationBrightness
from data import AppData

class ApplicationBrightnessSlider(Slider, ISlider[float]):
    def __init__(self, orientation: Qt.Orientation = Qt.Orientation.Horizontal):
        Slider.__init__(self, orientation)
        ISlider[float].setup(self, "apllication_brightness", "Apllication Brightness", 0, 0.9)
        self.setup()
    def setup(self):
        self.overlay = ApllicationBrightness.init()

        self.setMinimum(0)
        self.setMaximum(1000)
        self.setSingleStep(1)

        self.valueChanged.connect(self._on_value_changed)
        
        self.setValue(int(AppData.application_brightness * 1000))
        ApllicationBrightness.set_brightness(AppData.application_brightness)
    @Slot()
    def reset(self):
        value = AppData.get_default("application_brightness")
        self.setValue(value * 1000)
        ApllicationBrightness.set_brightness(value)
        AppData.application_brightness = value
    @Slot(int)
    def _on_value_changed(self, value: int):
        AppData.application_brightness = float(value) / 1000
        ApllicationBrightness.set_brightness(AppData.application_brightness)