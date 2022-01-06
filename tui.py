from time import sleep
from rich.console import Console
from rich.prompt import Prompt
from rich.console import Console
from rich.align import Align
from rich.text import Text
from rich.panel import Panel

from main import Player

plyr = Player()

console = Console()
with console.screen(style="#5050ff") as screen:
    name = Prompt.ask("Enter your name")
    text = Align.center(
    Text.from_markup(f"Hey welcome to Fabic!", justify="center"),
    vertical="middle",)
    screen.update(Panel(text))
    plyr.loop()
    '''while True:
        text = Align.center(
        Text.from_markup(f"Hey {name}!", justify="center"),
        vertical="middle",)
        screen.update(Panel(text))'''