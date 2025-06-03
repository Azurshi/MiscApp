from widgets import MainWindow
from items import TextLabel, TextButton
from layouts import GridLayout, ListLayout
from styles import Style
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

style = Style()


class App:
    def __init__(self):
        global style
        self.app = QApplication(sys.argv)
        self.window = MainWindow(None)
        
        
        style.background_color = "red"
        style.apply(self.window)
        self.label = TextLabel("wow")
        self.button = TextButton("button")
        self.button2 = TextButton("button2")
        self.list = ListLayout(orientation = Qt.Orientation.Horizontal)
        
        style.border = (4, "solid", "yellow")
        style.apply(self.list)
        style.border = None
        self.window.add_widget(self.list)
        self.list.add_widgets([self.label, self.button, self.button2]) #type:ignore
        
        style.background_color = "blue"
        style.apply(self.button)
        self.window.show()
    def exec(self):
        self.app.exec()
        

# style.margin = (1, 2)
# style.size_unit = 'px'
print(style.__evaluate())

app = App()
app.exec()