from app_controller.app import App

from apps.brightness.app import BrightnessApp, BrightnessData
from apps.keymap.app import KeymapApp, KeymapData

app = App()
print("Start")
app.setup()
apps = [
    (BrightnessApp, BrightnessData),
    (KeymapApp, KeymapData)
]
for app_tyle, app_data in apps:
    app.register_app(app_tyle, app_data)
app.set_connection()
app.exec()
print("End")