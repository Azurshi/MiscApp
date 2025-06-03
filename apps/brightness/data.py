from core import IAppData

class BrightnessData(IAppData):
    brightness = 1.0 # [0.5, 1]
    brightness_resolution = 1000 
    factor = 1.0
    factor_resolution = 1000
    factor_min = 0.1
    factor_max = 2