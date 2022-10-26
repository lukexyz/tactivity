from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Button, Static

class TimeDisplay(Static):
    """A widget to display elapsed time."""

class EmojiDisplay(Static):
    """A widget to display the stopwatch status"""

class Stopwatch(Static):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler"""
        if event.button.id == "start":
            self.add_class("started")
        elif event.button.id == "stop":
            self.remove_class("started")

    def compose(self) -> ComposeResult:
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")
        yield TimeDisplay("00:00:00.00")
        yield EmojiDisplay("🏃")

class StopwatchApp(App):
    "Textual app from the tutorial docs."

    CSS_PATH = "stopwatch.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield Container(Stopwatch(), Stopwatch())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

if __name__ == "__main__":
    app = StopwatchApp()
    app.run()