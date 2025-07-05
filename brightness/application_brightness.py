from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtCore import Qt, QTimer, Slot
import win32gui
from data import AppData
from typing import Self
MAX_OPACITY = 0.75

HNWD_NOTOPMOST = -2
HNWD_TOPMOST = -1
SWP_NOMOVE = 0x0002
SWP_NOSIZE = 0x0001
SWP_NOACTIVE = 0x0010
SWP_SHOWWINDOW = 0x0040
WIN32_FLAGS = SWP_NOMOVE | SWP_NOACTIVE | SWP_NOSIZE | SWP_SHOWWINDOW
class ApllicationBrightness(QMainWindow):
    instance: Self
    def __init__(self, parent: QWidget | None = None):
        if not hasattr(ApllicationBrightness, "instance"):
            ApllicationBrightness.instance = self
        else:
            raise Exception("Does not support multi instance")
        flags = Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.WindowTransparentForInput | Qt.WindowType.Tool
        super().__init__(parent, flags)
        self.setStyleSheet(ApllicationBrightness.__name__+ "{background-color : black;}")
        self.showFullScreen()
        # self.setWindowTitle(ApllicationBrightnessOverlayQT.__name__)
        self.force_timer = QTimer(self)
        self.force_timer.timeout.connect(self.force)
        self.force_timer.start(1000)
        self.last_fore_hwnd = 0
        self.set_brightness(0.5)
    @Slot()
    def force(self):
        fore_hwnd = win32gui.GetForegroundWindow()
        if fore_hwnd != self.last_fore_hwnd:
            self.last_fore_hwnd = fore_hwnd
            # print(fore_hwnd, AppData.app_hwnd)
            if fore_hwnd != AppData.app_hwnd:
                hwnd = self.winId()
                win32gui.SetWindowPos(
                    hwnd, HNWD_TOPMOST, 0, 0, 0, 0,
                    WIN32_FLAGS
                )
    @classmethod
    def set_brightness(cls, percent: float):
        percent = min(1, max(0, percent))
        percent = 1 - percent
        percent = min(MAX_OPACITY, percent)
        cls.instance.setWindowOpacity(percent)
    @classmethod
    def init(cls) -> "ApllicationBrightness":
        if not hasattr(ApllicationBrightness, "instance"):
            return ApllicationBrightness()
        else:
            return ApllicationBrightness.instance