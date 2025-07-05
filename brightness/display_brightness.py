import wmi

class DisplayBrightness:
    @classmethod
    def get_current_brightness(cls) -> float:
        wmi_interface = wmi.WMI(namespace="wmi")
        brightness_info = wmi_interface.WmiMonitorBrightness()[0]
        return float(brightness_info.CurrentBrightness) / 100
    @classmethod
    def set_brightness(cls, percent: float):
        percent = min(1, max(0, percent))
        brightness = int(percent * 100)
        wmi_interface = wmi.WMI(namespace="wmi")
        methods = wmi_interface.WmiMonitorBrightnessMethods()[0]
        methods.WmiSetBrightness(brightness, 0)        