from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport

__app_name__ = "wiki-cheatsheet"
__version__ = "0.0.1"

class cheatsheet: 
    def __init__(self): 
        self.url = "https://wiki.hades-cybersecurity.com/graphql"
        self.token = self.read_token_from_config_file()
        self.headers = {"Authorization": "Bearer {}".format(self.token)}
        self.config_path = self.get_config_path()
        self.cheatsheet_path = self.get_cheatsheet_path()
        self.db_config_path = self.get_db_config_path()
        self.transport = AIOHTTPTransport(url=self.url, headers=self.headers)
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

    from .config import (
        init_config, 
        get_config_path, 
        write_token,
        read_token_from_config_file, 
        get_cheatsheet_path, 
        get_db_config_path,
        init_local_db, 
        simulate_data
    )
    from .query import (
        query_graphql
    )

    from .tags import (
        get_tag_list
    )

    from .pages import (
        retrieve_page_by_id,
        get_page_id_by_tags,
        save_cheatsheet,
        get_all_pages
    )

    from .local_actions import (
        list_downloaded_cheatsheets
    )

    from .sqlite_cheatsheet import (
        insert_tag,
        insert_cheatsheet,
        insert_link_tag_cheatsheet,
        insert_all,
        search_cheatsheet_by_tag
    )

