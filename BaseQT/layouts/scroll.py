from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QFrame, QScrollArea, QStackedLayout
from typing import cast

class ScrollWrapper(QFrame):
    @property
    def qlayout(self) -> QStackedLayout:
        return cast(QStackedLayout, self.layout())
    def __init__(self, layout: QWidget, orientation: Qt.Orientation = Qt.Orientation.Vertical):
        super().__init__(None)
        self.central_widget = layout
        self.setLayout(QStackedLayout())
        self.layout().setSpacing(0) #type:ignore
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.central_widget)
        if orientation == Qt.Orientation.Vertical:
            self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        elif orientation == Qt.Orientation.Horizontal:
            self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.layout().addWidget(self.scroll_area) #type:ignore
