from time import sleep
from rich.console import Console
from rich.prompt import Prompt
from rich.console import Console
from rich.align import Align
from rich.text import Text
from rich.panel import Panel
from rich.layout import Layout

from main import Player

plyr = Player()

console = Console()
with console.screen(style="#5050ff") as screen:

    text = Align.center(
    Text.from_markup(f"Hey welcome to Fabic!", justify="center"),
    vertical="middle",)
    screen.update(Panel(text))
    path = Prompt.ask("Enter path to your music folder")
    plyr.open_folder(path)
    q = plyr.get_queue()
    q.play()
    layout = Layout()
    while True:
        plyr.event_handler()
        text = Align.center(
        Text.from_markup(f"{plyr.get_nowplaying_str()}\n{plyr.get_name_str()} {plyr.get_progress_str()}\n{plyr.get_loading_str()}", justify="center"),
        vertical="middle",)
        screen.update(Panel(text))