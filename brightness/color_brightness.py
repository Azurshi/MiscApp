import ctypes
import ctypes.wintypes
import math
from typing import Callable

class ColorRamp:
    @classmethod
    def _set_gamma_raw(cls, r, g, b):
        ramp = (ctypes.wintypes.WORD * 256 * 3)()
        for i in range(256):
            ramp[0][i] = r * i
            ramp[1][i] = g * i
            ramp[2][i] = b * i
        hDc = ctypes.windll.user32.GetDC(0)
        success = ctypes.windll.gdi32.SetDeviceGammaRamp(hDc, ctypes.byref(ramp))
        if (success):
            ctypes.windll.user32.ReleaseDC(0, hDc)
            return True
        else:
            ctypes.windll.user32.ReleaseDC(0, hDc)
            return False
    @classmethod
    def _set_gamma_percent(cls, r, g, b):
        def convert(percent):
            if (percent <= 1):
                return math.floor(percent * 128 + 128)
            else:
                return 512
        cls._set_gamma_raw(convert(r), convert(g), convert(b))
    @classmethod
    def _set_gamma_func(cls, device_factor, transform):
        ramp = (ctypes.wintypes.WORD * 256 * 3)()
        for i in range(256):
            x = math.ceil(max(0,min(256,transform(i) / device_factor)) * 256)
            ramp[0][i] = x
            ramp[1][i] = x
            ramp[2][i] = x
        hDc = ctypes.windll.user32.GetDC(0)
        success = ctypes.windll.gdi32.SetDeviceGammaRamp(hDc, ctypes.byref(ramp))
        if (success):
            ctypes.windll.user32.ReleaseDC(0, hDc)
            return True
        else:
            ctypes.windll.user32.ReleaseDC(0, hDc)
            return False
    @classmethod
    def set_gamma(cls, devide_factor : float, transform : Callable):
        return cls._set_gamma_func(devide_factor, transform)
    

class ColorBrightness:
    @classmethod
    def set_brightness(cls, percent: float):
        percent = min(1, max(0, percent))
        def transform(x):
            return (x/256)**(1) * 256
        # 0.5 -> 1
        ColorRamp.set_gamma(1/(percent*0.5+0.5), transform)
    
        