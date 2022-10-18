import sqlite3


def insert_tag(self, tag_id, tag_name):
    con = sqlite3.connect(self.db_config_path)
    cur = con.cursor()

    cur.execute("INSERT OR REPLACE INTO tags(tag_id, tag) VALUES ({}, '{}')".format(tag_id, tag_name))

    con.commit()
    con.close()


def insert_cheatsheet(self, cheatsheet_id, filename, title, description, cheatsheet_hash):
    con = sqlite3.connect(self.db_config_path)
    cur = con.cursor()

    cur.execute(
        "INSERT OR REPLACE INTO cheatsheets(cheatsheet_id, filename, title, description, hash) VALUES ({}, '{}', '{}', '{}', '{}');".format(
            cheatsheet_id, filename, title, description, cheatsheet_hash))

    con.commit()
    con.close()


def insert_link_tag_cheatsheet(self, cheatsheet_id, tag_id):
    con = sqlite3.connect(self.db_config_path)
    cur = con.cursor()

    cur.execute(
        "INSERT OR REPLACE INTO link_cheatsheets_tags(cheatsheet_id, tag_id) VALUES ({}, {})".format(cheatsheet_id, tag_id))

    con.commit()
    con.close()


def insert_all(self, cheatsheet_id, cheatsheet_hash, filename, title, description, list_tag):
    self.insert_cheatsheet(cheatsheet_id, filename, title, description, cheatsheet_hash)

    for tag in list_tag:
        self.insert_tag(tag["id"], tag["tag"])
        self.insert_link_tag_cheatsheet(cheatsheet_id, tag["id"])


def search_cheatsheet_by_tag(self, tag_id=-1, tag_name=None):
    if tag_id != -1:
        con = sqlite3.connect(self.db_config_path)
        cur = con.cursor()

        cur.execute("SELECT cheatsheet_id FROM link_cheatsheets_tags WHERE tag_id=8")
        rows = cur.fetchall()

        for row in rows:
            cur.execute("SELECT * FROM cheatsheets WHERE cheatsheet_id={}".format(row[0]))
            other_row = cur.fetchall()
            print(other_row)

        con.close()
