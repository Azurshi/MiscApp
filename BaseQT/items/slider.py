from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSlider

class Slider(QSlider):
    def __init__(self, orientation: Qt.Orientation = Qt.Orientation.Horizontal):
        super().__init__(orientation, None)
        
