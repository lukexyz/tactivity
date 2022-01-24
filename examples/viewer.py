import os
import sys
from rich.console import RenderableType

from rich.syntax import Syntax
from rich.traceback import Traceback

from textual.app import App
from textual.widgets import Header, Footer, FileClick, ScrollView, DirectoryTree


class MyApp(App):
    """Example of an interactive textual app"""

    async def on_load(self) -> None:
        """Sent before going into application mode"""

        # Bind keys
        await self.bind("b", "view.toggle('sidebar')", "Toggle sidebar")
        await self.bind("q", "quit", "Quit")

        # Get path to show
        try:
            self.path = sys.argv[1]
        except IndexError:
            self.path = os.path.abspath(
                os.path.join(os.path.basename(__file__), "../../"))
        
    async def on_mount(self) -> None:
        """call afer terminal goes into applicaiton mode"""
        
        # create widgets
        self.body = ScrollView()
        self.directory = DirectoryTree(self.path, "Code")

        # Dock the widgets
        await self.view.dock(Header(), edge="top")
        await self.view.dock(Footer(), edge='bottom')

        # Note the directory is also in a scroll view
        await self.view.dock(ScrollView(self.directory), edge='left', size=48, name='sidebar')
        await self.view.dock(self.body, edge='top')

    async def handle_file_click(self, message: FileClick) -> None:
        """A message sent by the directory tree when a file is clicked."""

        syntax: RenderableType
        try:
            # Construct a Syntax object for the path in the message
            syntax = Syntax.from_path(
                message.path,
                line_numbers=True,
                word_wrap=True,
                indent_guides=True,
                theme="monokai",
            )
        except Exception:
            # Possibly a binary file
            # For demonstration purposes we will show the traceback
            syntax = Traceback(theme="monokai", width=None, show_locals=True)
        self.app.sub_title = os.path.basename(message.path)
        await self.body.update(syntax)

MyApp.run(title='Code Viewer', log="textual.log")

