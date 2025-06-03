from typing import Type, cast

from PySide6.QtCore import Qt

from BaseQT import QWidget
from core.app_interface import IAppData
from .data import BrightnessData
from core import IApp
from BaseQT import *
from .color_ramp import ColorRamp
from .interface import BrightnessInterface

class BrightnessApp(IApp):
    app_name = "Brightness"
    def __init__(self) -> None:
        super().__init__()
    @classmethod
    def set_color_ramp(cls):
        data = BrightnessData
        def transform(x):
            return (x/256)**(data.factor) * 256
        ColorRamp.set_gamma(1/data.brightness, transform)
    @classmethod
    def start_background_process(cls):
        cls.set_color_ramp()
    @classmethod
    def get_foreground_interface(cls) -> QWidget:
        interface = BrightnessInterface()
        data = BrightnessData
        interface.factor_slider.setSingleStep(1)
        interface.factor_slider.setMinimum(int(data.factor_min * data.factor_resolution))
        interface.factor_slider.setMaximum(int(data.factor_max * data.factor_resolution))
        interface.factor_slider.setValue(int(data.factor * data.factor_resolution))
        interface.brightness_slider.setSingleStep(1)
        interface.brightness_slider.setMinimum(int(0.5 * data.brightness_resolution))
        interface.brightness_slider.setMaximum(int(1 * data.brightness_resolution))
        interface.brightness_slider.setValue(int(data.brightness * data.brightness_resolution))
        def change_brighness(value: int):
            data.brightness = float(value) / data.brightness_resolution
            cls.set_color_ramp()
        def change_factor(value: int):
            data.factor = float(value) / data.factor_resolution
            cls.set_color_ramp()
        def reset_brightness():
            data.brightness = 1
            interface.brightness_slider.setValue(int(data.brightness * data.brightness_resolution))
            cls.set_color_ramp()
        def reset_factor():
            data.factor = 1
            interface.factor_slider.setValue(int(data.factor * data.factor_resolution))
            cls.set_color_ramp()
        interface.brightness_slider.valueChanged.connect(change_brighness)
        interface.factor_slider.valueChanged.connect(change_factor)
        interface.brightness_reset_button.clicked.connect(reset_brightness)
        interface.factor_reset_button.clicked.connect(reset_factor)
        cls.set_color_ramp()
        return interface