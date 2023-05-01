from os import listdir


def list_downloaded_cheatsheets(self): 
    return listdir(self.cheatsheet_path)


def read_single_page_by_id(self, cheatsheet_id:int):
    infos = self.get_local_cheatsheet_info_by_id(cheatsheet_id)
    return infos[0]