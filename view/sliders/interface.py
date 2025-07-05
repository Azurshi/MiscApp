from typing import TypeVar, Any, Generic, cast

T = TypeVar("T")

class ISlider(Generic[T]):
    def setup(self, id: str, display_name: str, min_value: T, max_value: T) -> None:
        self.id = id
        self.name = display_name
        self.min_value = min_value
        self.max_value = max_value