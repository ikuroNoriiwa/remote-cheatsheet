from typing import Optional
import typer 
from . import wiki_cheatsheet
from .remote import app as remote_app
from .local import app as local_app
from .config import app as config_app

app = typer.Typer()
app.add_typer(remote_app, name="remote", help="Connect remote Host")
app.add_typer(local_app, name="local", help="Manage local cheatsheets")
app.add_typer(config_app, name="config", help="Configure app settings")

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



