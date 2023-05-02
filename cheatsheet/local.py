from typing import Optional, List
from typing_extensions import Annotated
import typer 
from . import wiki_cheatsheet
from rich.table import Table
from rich.console import Console
from rich import print as rprint 

app = typer.Typer()


@app.command()
def list():
    """
    List all local cheatsheets
    """
    cs = wiki_cheatsheet.cheatsheet()
    # lst_cheatsheets = cs.list_downloaded_cheatsheets()
    # for cheatsheet in lst_cheatsheets: 
    #     typer.echo(cheatsheet)
    
    table = Table(title="Local Cheatsheet list")
    table.add_column("ID", justify="center", no_wrap=True, style="cyan")
    table.add_column("Title", justify="left", )
    table.add_column("Description", justify="left", )
    table.add_column("Filename", justify="left", )
    pages = cs.list_all_local_cheatsheets()

    for page in pages: 
        table.add_row(str(page[0]), page[2], page[3], f"{page[1]}")
    console = Console()
    console.print(table)


@app.command()
def read(cheatsheet_id: Annotated[int, typer.Argument(default=..., metavar="id"), typer.Option(True)]):
    "Read a single downloaded cheatsheet by it's ID"
    cs = wiki_cheatsheet.cheatsheet()
    exist = cs.check_local_id(cheatsheet_id)
    console = Console()
    if exist:
        read_single_page = cs.read_single_page_by_id(cheatsheet_id)
        filename = f"{cs.cheatsheet_path}/{read_single_page[1]}"
        with open(filename, 'r') as file:
            for line in file: 
                if line.startswith('#'): 
                    console.print(line, end='', style="color(223)")
                else: 
                    console.print(line, end='')
            console.print()
