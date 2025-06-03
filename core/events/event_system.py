from .weak_event_handler import WeakEventHandler
from typing import Callable, Type, TypeVar

class EventArgs:
    pass
TEventArgs = TypeVar("TEventArgs", bound=EventArgs)
class EventSystem:
    __handlers: dict[type, WeakEventHandler] = {}
    @classmethod
    def connect(cls, arg_type: Type[TEventArgs], handler: Callable[[TEventArgs], None]):
        class_handler = cls.__handlers.get(arg_type, None)
        if class_handler is None:
            class_handler = WeakEventHandler()
            class_handler.add_handler(handler)
            cls.__handlers[arg_type] = class_handler
        else:
            class_handler.add_handler(handler)
    @classmethod
    def publish(cls, arg: EventArgs):
        arg_type = type(arg)
        class_handler = cls.__handlers.get(arg_type, None)
        if class_handler is not None:
            class_handler.invoke(arg)