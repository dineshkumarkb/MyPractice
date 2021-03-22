# Import the console API
from rich.console import Console
from rich import print as rprint
from rich.table import Table
import time

style1 = "bold red on yellow"
console = Console(color_system="auto")

def initiate_wait():
    time.sleep(3)

def display_table():

    time.sleep(2)
    t = Table(title="Nolan Filmography", title_justify="center")
    t.add_column("Movie", justify="center", style="cyan")
    t.add_column("Year", justify="center", style="cyan")
    t.add_row("Tenet", "2021")
    t.add_row("Dunkirk", "2017")
    t.add_row("Intersteller", "2014")
    t.add_row("Inception", "2010")
    console.print(t)

def start_cli():
    console.rule()
    console.print(" ......... Welcome to the command line built using rich .........", style=style1, justify="center")
    console.rule()
    with console.status(spinner="arc", status="Initiating.."):
        console.log(" Initiating wait ")
        initiate_wait()
        console.log(" Wait complete ")
    username = console.input("Please enter [blue]your[/blue] [yellow]username[/yellow]: ")
    console.log(f"User name received [red]{username}[/red]")
    console.print(f" Welcome [yellow]{username}[/yellow] !!! ")

    with console.status(spinner="arc", status="Loading.."):
        display_table()



if __name__ == "__main__":
    start_cli()
