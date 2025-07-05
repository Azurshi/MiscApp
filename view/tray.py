from BaseQT import *
from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QApplication
from PySide6.QtGui import QAction, QIcon

class SystemTray(QSystemTrayIcon):
    tray_left_clicked = Signal()
    tray_double_clicked = Signal()
    tray_right_clicked = Signal()
    open_selected = Signal()
    close_selected = Signal()
    exit_selected = Signal()
    def __init__(self, icon: QIcon, parent: QWidget | QApplication):
        super().__init__(icon, parent)
        self.setToolTip("Brightness")
        self.tray_menu = QMenu()
        self.setContextMenu(self.tray_menu)
        self.add_action()
        # self.activated.connect(lambda: self.geometry().center())
        self.activated.connect(self.on_tray_activated)        
        self.tray_menu.show()
        self.show()
    def add_action(self):
        open_action = QAction("Open", self.tray_menu)
        close_action = QAction("Close", self.tray_menu)
        exit_action = QAction("Exit", self.tray_menu)
        self.tray_menu.addActions([
            open_action, close_action, exit_action
        ])
        open_action.triggered.connect(self.open_selected)
        close_action.triggered.connect(self.close_selected)
        exit_action.triggered.connect(self.exit_selected)
    def on_tray_activated(self, reason: QSystemTrayIcon.ActivationReason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.tray_left_clicked.emit()
        elif reason == QSystemTrayIcon.ActivationReason.Context:
            self.tray_right_clicked.emit()
        elif reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            self.tray_double_clicked.emit()
