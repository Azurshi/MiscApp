import keyboard

class Keymap:
    @classmethod
    def set_data(cls, data: list[tuple[str, str]]) -> list[tuple[str, str]]:
        keyboard.unhook_all()
        valid_data: list[tuple[str, str]] = []
        for from_key, to_key in data:
            try:
                keyboard.remap_key(from_key, to_key)
                valid_data.append((from_key, to_key))
            except:
                print(f"Invalid key {from_key} -> {to_key}")
        return valid_data
    @classmethod
    def clear(cls):
        keyboard.unhook_all()