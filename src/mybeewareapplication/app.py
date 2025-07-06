<<<<<<< HEAD
"""
A simple BeeWare application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class MyBeeWareApplication(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return MyBeeWareApplication()
=======
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

class MyBeewareApplication(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)

        self.label = toga.Label("0", style=Pack(text_align=CENTER))
        self.button = toga.Button("Push me!", on_press=self.on_button_press, style=Pack(padding=5))

        box = toga.Box(
            children=[
                self.label,
                self.button,
            ],
            style=Pack(direction=COLUMN, alignment=CENTER, padding=10)
        )

        self.main_window.content = box
        self.main_window.show()
        self.counter = 0

    def on_button_press(self, widget):
        self.counter += 1
        self.label.text = str(self.counter)

def main():
    return MyBeewareApplication()
>>>>>>> 19df0c4 (Add basic counter app and docs)
