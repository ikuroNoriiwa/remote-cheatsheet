from lib2to3.pgen2 import token
from os.path import exists, join
from os import getenv, makedirs
from platform import system
import sqlite3

if system() is "Windows":
    DEFAULT_CONFIG_PATH = r"{}\.wiki-cheatsheet".format(getenv("HOMEPATH"))
elif system() is "Linux":
    DEFAULT_CONFIG_PATH = r"{}/.wiki-cheatsheet".format(getenv("HOME"))
else:
    DEFAULT_CONFIG_PATH = r"{}/.wiki-cheatsheet".format(getenv("HOME"))

def init_config(self, config_path=DEFAULT_CONFIG_PATH, token=None): 
    print(config_path)
    print(exists(config_path))
    if exists(config_path) is False: 
        makedirs(self.get_cheatsheet_path(), exist_ok=True)
        print("Successfuly created config dir : {}".format(config_path))

        if token is None: 
            self.write_token("xxxx.yyyyy.zzzzz")
        else: 
            self.write_token(token)

        print("Create config database")
        self.init_local_db()
        print("Done")

def get_config_path(self): 
    return DEFAULT_CONFIG_PATH

def get_cheatsheet_path(self):
    return join(DEFAULT_CONFIG_PATH, "cheatsheet")

def get_db_config_path(self):
    return join(DEFAULT_CONFIG_PATH, "search.db")

def write_token(self, token:str):
    config_path = self.get_config_path()
    
    with open(join(config_path, "token.md"), "w") as file: 
        file.write(token.replace("\r", "").replace("\n", "").replace(" ", ""))

def read_token_from_config_file(self): 
    if exists(join(self.get_config_path(), "token.md")): 
        with open(join(self.get_config_path(), "token.md"), 'r') as token: 
            token = token.read()
    else: 
        token = None 

    return token

def init_local_db(self): 
    if exists(self.db_config_path) is False: 
        con = sqlite3.connect(self.db_config_path)
        cur = con.cursor()

        cur.execute("CREATE TABLE cheatsheets(cheatsheet_id INTEGER PRIMARY KEY, filename, title, description, hash)")
        cur.execute("CREATE TABLE tags(tag_id INTEGER PRIMARY KEY, tag)")
        cur.execute("CREATE TABLE link_cheatsheets_tags(cheatsheet_id, tag_id, FOREIGN KEY (cheatsheet_id) REFERENCES cheatsheets(cheatsheet_id), FOREIGN KEY (tag_id) REFERENCES tags(tag_id)) ")

        con.close()
        
def simulate_data(self): 
    con = sqlite3.connect(self.db_config_path)
    cur = con.cursor()

    cur.execute("INSERT INTO cheatsheets(cheatsheet_id, filename, title, description, hash) VALUES (13, 'patator.md', 'patator', 'description', 'hash');")
    cur.execute("INSERT INTO tags(tag_id, tag) VALUES (8, 'enum')")
    cur.execute("INSERT INTO link_cheatsheets_tags(cheatsheet_id, tag_id) VALUES (13, 8)")
    con.commit()
    con.close()


