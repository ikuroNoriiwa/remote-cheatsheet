from threading import local
from typing import Optional, List
import typer 
import wiki_cheatsheet
from cli.remote import app as remote_app 
from cli.local import app as local_app 

app = typer.Typer()
app.add_typer(remote_app, name="remote")
app.add_typer(local_app, name="local")

def _version_callback(value:bool) -> None: 
    if value:
        typer.echo(f"{wiki_cheatsheet.__app_name__} v{wiki_cheatsheet.__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return



