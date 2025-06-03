from typing import Type, cast

from PySide6.QtCore import Qt

from core.app_interface import IAppData
from core import IApp
from BaseQT import *

import keyboard
from .data import KeymapData
from .interface import KeymapInterface
from .keymap import Keymap
import weakref

class KeymapApp(IApp):
    app_name = "Keymap"
    current_interface: weakref.ReferenceType[KeymapInterface] | None = None
    def __init__(self) -> None:
        super().__init__()
    @classmethod
    def start_background_process(cls):
        cls.__refresh()
    @classmethod
    def on_key_event(cls, event: keyboard.KeyboardEvent):
        if keyboard.is_pressed("alt") and event.event_type == "down" and event.name == "q":
            KeymapData.is_active = not KeymapData.is_active
            cls.__refresh()
            # print(f"Keymap state: {KeymapData.is_active}")
    @classmethod
    def __refresh(cls):
        if cls.current_interface != None:
            interface = cls.current_interface()
            if interface != None:
                interface.status_label.setText("On" if KeymapData.is_active else "Off")
            else:
                cls.current_interface = None
        if KeymapData.is_active:
            Keymap.set_data(KeymapData.key_map)
        else:
            Keymap.clear()
        keyboard.hook(cls.on_key_event)
    @classmethod
    def get_foreground_interface(cls) -> QWidget:
        interface = KeymapInterface()
        interface.key_list.set_data(KeymapData.key_map)
        def on_key_applied():
            valid_data = Keymap.set_data(interface.key_list.get_data())
            interface.key_list.set_data(valid_data)
            KeymapData.key_map = valid_data
            keyboard.hook(cls.on_key_event)
        def on_key_canceled():
            interface.key_list.set_data(KeymapData.key_map)
        interface.key_applied.connect(on_key_applied)
        interface.key_canceled.connect(on_key_canceled)
        interface.status_label.setText("On" if KeymapData.is_active else "Off")
        cls.current_interface = weakref.ref(interface)
        return interface