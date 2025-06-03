from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy
from PySide6.QtGui import QPixmap, QResizeEvent, QImage, QMouseEvent
import base64

class ImageLabel(QLabel):
    mouse_pressed = Signal()
    def __init__(self, text: str = ""):
        super().__init__(text)
        self.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pixmap_ : QPixmap | None = None
    def set_image(self, image_data_str : str):
        image = QImage.fromData(base64.b64decode(image_data_str))
        self.pixmap_ = QPixmap.fromImage(image)
        self._set_pixmap()
    def _set_pixmap(self):
        if self.pixmap_ == None: return
        width = self.width()
        height = self.height()
        scaled_pixmap = self.pixmap_.scaled(width,height,Qt.AspectRatioMode.KeepAspectRatio,Qt.TransformationMode.SmoothTransformation)
        self.setPixmap(scaled_pixmap)
    def set_pixmap(self, pixmap : QPixmap | None):
        self.pixmap_ = pixmap
        self._set_pixmap()
    # def load_and_set_pixmap(self, path : str):
    #     self.pixmap_ = QPixmap(path)
    #     self._set_pixmap()
    def resizeEvent(self, event : QResizeEvent):
        if self.pixmap_ != None and  not self.pixmap_.isNull():
            self._set_pixmap()
        super().resizeEvent(event)
    def mousePressEvent(self, ev: QMouseEvent):
        self.mouse_pressed.emit()
        ev.accept()

