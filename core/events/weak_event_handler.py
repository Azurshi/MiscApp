from typing import Callable, Any
import weakref

class WeakEventHandler:
    def __init__(self):
        super().__init__()
        self.__handlers: list[weakref.WeakMethod | Callable] = []
    def add_handler(self, handler: Callable[[Any], None]):
        if hasattr(handler, "__self__") and handler.__self__ is not None:
            self.__handlers.append(weakref.WeakMethod(handler))
        else:
            self.__handlers.append(handler)

    def invoke(self, arg: object):
        dead_handler_indexes: list[int] = []
        for index, ref in enumerate(self.__handlers):
            if isinstance(ref, weakref.WeakMethod):
                handler: Callable | None = ref()
                if handler is None:
                    dead_handler_indexes.append(index)
                else:
                    handler(arg)
            else:
                ref(arg)
        for index in reversed(dead_handler_indexes):
            self.__handlers.pop(index)