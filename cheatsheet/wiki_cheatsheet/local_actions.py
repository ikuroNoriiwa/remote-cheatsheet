from os import listdir

def list_downloaded_cheatsheets(self): 
    return listdir(self.cheatsheet_path)