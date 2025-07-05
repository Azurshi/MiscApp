import os, json
from typing import Any, TypeVar, Generic, Optional, Type, cast
T = TypeVar("T")

class DataField(Generic[T]):
    _file_path: str = "data.json"
    _data: dict[str, Any] = {}
    def __init__(self, default_value: T) -> None:
        super().__init__()
        self._field_name: str = ""
        self._default_value: T = default_value
    def __set_name__(self, owner: Type["AppData"], name: str):
        self._field_name = name
    def __get__(self, instance: Optional["AppData"], owner: Type["AppData"]) -> T:
        return cast(T, DataField._data.get(self._field_name, self._default_value))
    def _set_(self, instance: Optional["AppData"], owner: Type["AppData"], value: T) -> None:
        DataField._data[self._field_name] = value
        DataField.save()
    def __set__(self, instance: Optional["AppData"], value: T) -> None:
        raise Exception("Instance access is not permitted") # For type hint only
    @classmethod
    def save(cls):
        with open(DataField._file_path, 'w') as file:
            file.write(json.dumps(DataField._data))
        # print("Data saved")
class AppDataMeta(type):
    def __new__(cls, name: str, bases: tuple[type, ...], dct: dict):
        if name != "AppData": 
            raise NotImplementedError("Only support for AppData class")
        if os.path.exists(DataField._file_path):
            with open(DataField._file_path, 'r') as file:
                data = json.loads(file.read())
            DataField._data = data
            print("Data loaded")
        return super().__new__(cls, name, bases, dct)
    def __setattr__(cls, name: str, value: Any) -> None:
        if cls is AppData: 
            obj = cls.__dict__.get(name)
            if isinstance(obj, DataField):
                return obj._set_(cls, AppData, value)
        return super().__setattr__(name, value)
class AppData(metaclass=AppDataMeta):
    color_brightness = DataField[float](1)
    application_brightness = DataField[float](1)
    app_hwnd = 0
    @classmethod
    def get_default(cls, field_name: str) -> Any:
        return cast(DataField, cls.__dict__[field_name])._default_value
    @classmethod
    def save(cls):
        DataField.save()