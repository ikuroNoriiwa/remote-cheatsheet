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
        table.add_row(str(page['cheatsheet_id']), page['title'], page['description'], f"{page['filename']}")
    console = Console()
    console.print(table)


@app.command()
def read(cheatsheet_id: Annotated[int, typer.Argument(default=..., metavar="id"), typer.Option(True)]):
    "Read a single downloaded cheatsheet by it's [green]ID[/green]"
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

@app.command()
def search_term(term: Annotated[List[str], typer.Argument(default=..., metavar="term")],
              title: Annotated[bool, typer.Option(default=True, help="")]=True,
              description: Annotated[bool, typer.Option(default=True, help="")]=True):
    cs = wiki_cheatsheet.cheatsheet()
    ids = []
    if title: 
        tmp = cs.search_term_in_name(term[0])
        [ids.append(id['cheatsheet_id']) for id in tmp]
    
    if description: 
        tmp = cs.search_term_in_description(term[0])
        [ids.append(id['cheatsheet_id']) for id in tmp]


    data_all = []
    if len(ids) > 0: 
        for id in set(ids): 
            page = cs.get_local_cheatsheet_info_by_id(id)
            data_all.append(page)

    table = Table(title="Local Cheatsheet list")
    table.add_column("ID", justify="center", no_wrap=True, style="cyan")
    table.add_column("Title", justify="left", )
    table.add_column("Description", justify="left", )
    table.add_column("Filename", justify="left", )
    pages = cs.list_all_local_cheatsheets()

    for page in data_all: 
        table.add_row(str(page['cheatsheet_id']), page['title'], page['description'], f"{page['filename']}")
    console = Console()
    console.print(table)

@app.command()
def tag_list(): 
    cs = wiki_cheatsheet.cheatsheet()
    tags = cs.get_list_tag()

    table = Table(title="Local tags list")
    table.add_column("ID", justify="center", no_wrap=True, style="cyan")
    table.add_column("Tag Name", justify="left", )

    for tag in tags: 
        table.add_row(str(tag['tag_id']), tag['tag'])
    console = Console()
    console.print(table)

@app.command()
def tags_seets(tag: Annotated[int, typer.Argument(default=..., metavar="tag")]):
    print(tag)
