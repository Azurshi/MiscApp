from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QDateEdit, QDateTimeEdit

class DateEdit(QDateEdit):
    def __init__(self):
        super().__init__()

class DateTimeEdit(QDateTimeEdit):
    def __init__(self):
        super().__init__()  