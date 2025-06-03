from core import IAppData

class KeymapData(IAppData):
    is_active = False
    key_map: list[tuple[str, str]] = []
    