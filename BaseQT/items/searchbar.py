from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QSlider, QLineEdit, QCompleter

class SearchBar(QLineEdit):
    def __init__(self, text: str = "", placeholder: str = "", suggestions: list[str] = []):
        super().__init__(text, None)
        self.set_suggestions(suggestions)
        self.setPlaceholderText(placeholder)
    def set_suggestions(self, suggestions: list[str]):
        self._completer = QCompleter(suggestions, self)
        self._completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self._completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.setCompleter(self._completer)

