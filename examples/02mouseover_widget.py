from textual.app import App
from textual import events
from textual.widgets import Header, Footer, Placeholder

class SimpleApp(App):

    async def on_load(self, event: events.Load) -> None:
        """Bind keys with the app loads (but before entering application mode)"""
        await self.bind("b", "view.toggle('sidebar')", "Toggle sidebar")
        await self.bind("q", "quit", "Quit")

    async def on_mount(self) -> None:

        # Header / footer / dock
        await self.view.dock(Header(), edge="top")
        await self.view.dock(Footer(), edge="bottom")
        await self.view.dock(Placeholder(), edge="left", size=30, name="sidebar")

        await self.view.dock(Placeholder())

SimpleApp.run(log="textual.log", title='custom widget')