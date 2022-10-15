import typer
from . import wiki_cheatsheet

app = typer.Typer()

@app.command()
def token():
    """
    Print configured token
    """
    cs = wiki_cheatsheet.cheatsheet()
    token = cs.read_token_from_config_file()
    typer.echo(f"your token : {token}")
    raise typer.Exit()

@app.command()
def set_token(token: str):
    """
    Set new token - erase old one if exists
    """
    cs = wiki_cheatsheet.cheatsheet()
    cs.write_token(token)
    typer.echo("Your token is now set")

@app.command()
def init_config(token: str):
    """
    init configuration folder
    """
    cs = wiki_cheatsheet.cheatsheet()
    cs.init_config(token=token)
    typer.echo("Your token is now set")
