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