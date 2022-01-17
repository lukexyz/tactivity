from textual.app import App
from textual.widgets import Placeholder

class SimpleApp(App):
    async def on_mount(self) -> None:
        await self.view.dock(Placeholder())

SimpleApp.run(log="textual.log")