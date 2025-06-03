from core import ISerializable
from typing import TypeVar, Type
import weakref
from BaseQT import QWidget

class IAppData(ISerializable): pass
TAppData = TypeVar("TAppData", bound=IAppData)
class IApp:
    app_name: str = "IApp"
    def __init__(self) -> None: pass
    @classmethod
    def start_background_process(cls): pass
    @classmethod
    def pause_background_process(cls): pass
    @classmethod
    def stop_background_process(cls): pass
    @classmethod
    def get_foreground_interface(cls) -> QWidget: raise NotImplementedError()
