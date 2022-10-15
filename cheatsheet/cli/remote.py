from typing import Optional, List
import typer 
import wiki_cheatsheet

app = typer.Typer()

@app.command()
def token():
    cs = wiki_cheatsheet.cheatsheet()
    token = cs.read_token_from_config_file()
    typer.echo(f"your token : {token}")
    raise typer.Exit()


@app.command()
def list_tags(): 
    cs = wiki_cheatsheet.cheatsheet()
    tags = cs.get_tag_list()
    for tag in tags: 
        print(tag)

@app.command()
def search_page_by_tag(tags:List[str]):
    cs = wiki_cheatsheet.cheatsheet()
    pages = cs.get_page_id_by_tags(tags)
    header = "|{:^8}|{:^15}|{:^40}|{:^50}|".format("ID", "Title", "Description", "Path")
    print(header)
    for i in range(len(header)): print("-", end="")
    print()
    for page in pages: 
        print("|{:^8d}|{:^15}|{:^40}|{:^50}|".format(page['id'], page["title"], page["description"], page["path"]))

@app.command()
def download(cheatsheet_id:int):
    cs = wiki_cheatsheet.cheatsheet()
    title, description, content, err = cs.retrieve_page_by_id(cheatsheet_id)
    cs.save_cheatsheet(title, description, content)
    




