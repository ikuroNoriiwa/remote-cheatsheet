import sqlite3

#cur.execute("
# ")
#cur.execute("INSERT INTO tags(tag_id, tag) VALUES (8, 'enum')")
#cur.execute("INSERT INTO link_cheatsheets_tags(cheatsheet_id, tag_id) VALUES (13, 8)")

def insert_tag(self, tag_id, tag_name): 
    con = sqlite3.connect(self.db_config_path)
    cur = con.cursor()

    cur.execute("INSERT INTO tags(tag_id, tag) VALUES ({}, '{}')".format(tag_id, tag_name))

    con.commit()
    con.close()

def insert_cheatsheet(self, cheatsheet_id, filename, title, description, hash): 
    con = sqlite3.connect(self.db_config_path)
    cur = con.cursor()

    cur.execute("INSERT INTO cheatsheets(cheatsheet_id, filename, title, description, hash) VALUES ({}, '{}', '{}', '{}', '{}');".format(cheatsheet_id, filename, title, description, hash))

    con.commit()
    con.close()

def insert_link_tag_cheatsheet(self, cheatsheet_id, tag_id): 
    con = sqlite3.connect(self.db_config_path)
    cur = con.cursor()

    cur.execute("INSERT INTO link_cheatsheets_tags(cheatsheet_id, tag_id) VALUES ({}, {})".format(cheatsheet_id, tag_id))

    con.commit()
    con.close()