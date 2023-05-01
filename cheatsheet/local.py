from typing import Optional, List
import typer 
from . import wiki_cheatsheet

app = typer.Typer()


@app.command()
def list():
    cs = wiki_cheatsheet.cheatsheet()
    lst_cheatsheets = cs.list_downloaded_cheatsheets()
    for cheatsheet in lst_cheatsheets: 
        typer.echo(cheatsheet)


@app.command()
def read(cheatsheet_id):
    cs = wiki_cheatsheet.cheatsheet()
    exist = cs.check_local_id(cheatsheet_id)

    if exist:
        read_single_page = cs.read_single_page_by_id(cheatsheet_id)
        filename = f"{cs.cheatsheet_path}/{read_single_page[1]}.md"
        with open(filename, 'r') as file:
            print(file.read())
