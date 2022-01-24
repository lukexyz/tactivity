from datetime import datetime
from rich.panel import Panel
from rich.align import Align
from textual.app import App
from textual import events
from textual.reactive import Reactive
from textual.widget import Widget
from textual.widgets import Header, Footer, Placeholder


class Blobber(Widget):
    mouse_over = Reactive(False)
    render_title = "Select Function"

    def render(self) -> Panel:
        #self.render_title = "Select Function"
        return Panel(self.render_title, style=("on cyan" if self.mouse_over else ""))
        
    def on_enter(self) -> None:
        self.mouse_over = True
        self.render_title = "SELECTION YOUR OPTIONS"
        return Panel(self.render_title, style=("on cyan" if self.mouse_over else ""))

    def on_leave(self) -> None:
        self.mouse_over = False
        self.render_title = "Select Function"


class Clock(Widget):

    def on_mount(self):
        self.set_interval(1, self.refresh)

    def render(self):
        time = datetime.now().strftime("%c")
        return Align.center(time, vertical="middle")


class ClockApp(App):
    async def on_load(self, event: events.Load) -> None:
        """Bind keys with the app loads (but before entering application mode)"""
        await self.bind("b", "view.toggle('sidebar')", "Toggle sidebar")
        await self.bind("q", "quit", "Quit")

    async def on_mount(self):
        # Header / footer / dock
        await self.view.dock(Header(), edge="top")
        await self.view.dock(Footer(), edge="bottom")
        await self.view.dock(Blobber(), edge="left", size=30, name="sidebar")
        await self.view.dock(Clock())

ClockApp.run(title='timer')
