import json
import os
from typing import TypeVar, Type

def Converter(ori_value: object, loaded_value: object) -> object:
    if isinstance(ori_value, tuple):
        loaded_value = tuple(loaded_value) #type:ignore
    return loaded_value

TSerializable = TypeVar("TSerializable", bound="ISerializable")
class ISerializable:
    __skip_fields__ = ("__annotations__", "__module__", "__doc__")
    __init__result = None
    __subclasses: list[Type["ISerializable"]] = []
    @classmethod
    def __init_class__(cls):
        if not os.path.exists(ISerializable.DataPath): os.mkdir(ISerializable.DataPath)
        return True
    DataPath = "UserData"
    def __init_subclass__(cls) -> None:
        if ISerializable.__init__result == None:
            ISerializable.__init__result = ISerializable.__init_class__()
        ISerializable.__subclasses.append(cls)
        
        file_path = os.path.join(ISerializable.DataPath, f"{cls.__name__}.json")
        # If exist, load saved values
        if os.path.exists(file_path):
            data: dict[str, object] = {}
            try: # Try to load
                with open(file_path, "r") as file:
                    data = json.loads(file.read())
            except Exception as e: # Exception, save intial values and return
                print(f"Error when tried to load {cls.__name__}: {e}")
                cls.save() 
                return
            # Apply value if load success
            need_save = False # Flag, save if encouter missing field in save file
            for field in cls.__dict__:
                if field in ISerializable.__skip_fields__: continue
                value = cls.__dict__[field]
                if isinstance(value, classmethod): continue
                if field in data:
                    loaded_value = Converter(value, data[field])
                    setattr(cls, field, loaded_value)
                else:
                    print(f"{cls.__name__} field {field} not exist, create new")
                    need_save = True
            if need_save:
                cls.save()
        # If not exist, save intial values and return
        else:
            print(f"{cls.__name__} data does not exists, create new")
            cls.save()
            return
    @classmethod
    def dump(cls: Type[TSerializable]) -> dict[str, object]:
        result: dict[str, object] = {}
        for field in cls.__dict__:
            if field in ISerializable.__skip_fields__: continue
            value = cls.__dict__[field]
            if isinstance(value, classmethod): continue
            result[field] = value
        return result
    @classmethod
    def save(cls: Type[TSerializable]):
        if cls is ISerializable: return
        with open(os.path.join(ISerializable.DataPath, f"{cls.__name__}.json"), "w") as file:
            file.write(json.dumps(cls.dump()))
        print(f"{cls.__name__} saved")
    @classmethod
    def save_all(cls: Type["ISerializable"]):
        for child_cls in ISerializable.__subclasses:
            child_cls.save()
