from typer.testing import CliRunner

from cheatsheet.wiki_cheatsheet import __app_name__, __version__
from cheatsheet import sub_cli

runner = CliRunner()

def test_version():
    result = runner.invoke(sub_cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout