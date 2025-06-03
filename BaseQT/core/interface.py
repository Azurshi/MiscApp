from typing import Callable

class IKeyView:
    @property
    def key(self) -> str | None:
        return self._key
    @key.setter
    def key(self, value: str | None) -> None:
        self._key = value
        if self._key is None:
            self.set_value(None)
        else:
            self.set_value(self._get_value_func(self._key))
    def __init__(self) -> None:
        self._key: str | None = None
        self._get_value_func: Callable[[str], str] = self._key_passing_func
    def _key_passing_func(self, key: str) -> str:
        return key
    def set_value(self, value: str | None) -> None:
        pass
    
class IKeysView:
    @property
    def keys(self) -> list[str]:
        return self._keys
    @keys.setter
    def keys(self, value: list[str]) -> None:
        self._keys = value
        if self._keys is None:
            self.set_value([])
        else:
            values = [self._get_value_func(key) for key in self._keys]
            self.set_value(values)
    def __init__(self) -> None:
        self._keys: list[str] = []
        self._get_value_func: Callable[[str], str] = self._key_passing_func
    def _key_passing_func(self, key: str) -> str:
        return key
    def set_value(self, values: list[str]) -> None:
        pass