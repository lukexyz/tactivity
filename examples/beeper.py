from textual.app import App


class ColorChanger(App):
    def on_key(self, event):
        if event.key.isdigit():
            self.background = f"on color({event.key})"
        if event.key == '2':
            self.console.bell()


ColorChanger.run(log="textual.log")