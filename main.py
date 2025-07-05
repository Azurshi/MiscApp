from view import App
from data import AppData



app = App()
print("Start")
app.setup()
app.set_connection()
app.exec()
print("End")