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