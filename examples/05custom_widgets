from rich.panel import Panel
from textual import events
from textual.app import App
from textual.reactive import Reactive
from textual.widget import Widget
from textual.widgets import Header, Footer, Placeholder


class Hover(Widget):

    mouse_over = Reactive(False)

    def render(self) -> Panel:
        return Panel("Hello [b]World[/b]", style=("on red" if self.mouse_over else ""))

    def on_enter(self) -> None:
        self.mouse_over = True
        return Panel("Hello [b]World[/b]", style=("on red" if self.mouse_over else ""))

    def on_leave(self) -> None:
        self.mouse_over = False


class HoverApp(App):
    """Demonstrates custom widgets"""

    async def on_load(self, event: events.Load) -> None:
             """Bind keys with the app loads (but before entering application mode)"""
             await self.bind("b", "view.toggle('sidebar')", "Toggle sidebar")
             await self.bind("q", "quit", "Quit")

    

    async def on_mount(self) -> None:

        await self.bind("q", "quit", "Quit")

        await self.view.dock(Header(), edge="top")
        hovers = (Hover() for _ in range(6))

        await self.view.dock(*hovers, edge="top")
        await self.view.dock(Footer(), edge="bottom")


HoverApp.run(log="textual.log")