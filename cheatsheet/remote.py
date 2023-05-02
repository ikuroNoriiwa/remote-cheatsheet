from typing import Optional, List
import typer
from . import wiki_cheatsheet
from rich.console import Console
from rich.table import Table
from rich.progress import track


app = typer.Typer()


@app.command()
def list_tags():
    cs = wiki_cheatsheet.cheatsheet()
    tags = cs.get_tag_list()
    for tag in tags:
        print(tag)


@app.command()
def search_page_by_tag(tags: List[str]):
    cs = wiki_cheatsheet.cheatsheet()
    lst_page = []
    for tag in tags:
        lst_page.append(cs.get_page_id_by_tags(tag))

    table = Table(title="Cheatsheet list for tags : {}".format(tags))
    table.add_column("ID", justify="center", no_wrap=True, style="cyan")
    table.add_column("Title", justify="left", )
    table.add_column("Description", justify="left", )
    table.add_column("Path", justify="left", )

    for pages in lst_page:
        for page in pages:
            table.add_row(str(page['id']), page["title"], page["description"], page["path"])
    console = Console()
    console.print(table)


@app.command()
def list_all():
    cs = wiki_cheatsheet.cheatsheet()
    pages = cs.get_all_pages()

    table = Table(title="Cheatsheet list")
    table.add_column("ID", justify="center", no_wrap=True, style="cyan")
    table.add_column("Title", justify="left", )
    table.add_column("Description", justify="left", )
    table.add_column("Path", justify="left", )

    for page in pages:
        table.add_row(str(page['id']), page["title"], page["description"], page["path"])
    console = Console()
    console.print(table)


@app.command()
def download(cheatsheet_id: int):
    cs = wiki_cheatsheet.cheatsheet()
    title, description, content, tag, hash_file, err = cs.retrieve_page_by_id(cheatsheet_id)
    cs.save_cheatsheet(title, description, content)
    filename = title.replace(" ", "_") + ".md"
    cs.insert_all(cheatsheet_id, hash_file, filename, title, description, tag)


@app.command()
def download_all():
    cs = wiki_cheatsheet.cheatsheet()
    pages = cs.get_all_pages()
    max_page = len(pages)

    current = 0
    for value in track(pages, description="Downloading pages ..."):
        title, description, content, tag, hash_file, err = cs.retrieve_page_by_id(value['id'])
        cs.save_cheatsheet(title, description, content)
        filename = title.replace(" ", "_") + ".md"
        cs.insert_all(value['id'], hash_file, filename, title, description, tag)
        current += 1

    print(f"Downloaded {current} pages on {max_page}")


@app.command()
def test():
    cs = wiki_cheatsheet.cheatsheet()
    cs.search_cheatsheet_by_tag(8)