from rich.panel import Panel

from textual.app import App
from textual.reactive import Reactive
from textual.widget import Widget


class Hover(Widget):
    
    mouse_over = Reactive(False)

    def render(self) -> Panel:
        style_colour = f"on cyan" if self.mouse_over else ""
        text = "WAGWAN [b]MY BROTHERS[/b]" if self.mouse_over else "Hello World"
        return Panel(text, style=(style_colour))

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False


class HoverApp(App):
    """demonstrates custom widgets"""

    async def on_mount(self) -> None:
        hovers = (Hover() for _ in range(5))
        await self.view.dock(*hovers, edge='top')

    async def on_load(self, event):
        await self.bind("q", "quit")

HoverApp.run(log="textual.log")