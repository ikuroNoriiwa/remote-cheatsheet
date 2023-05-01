from typing import Type
from gql import gql
from gql.transport.exceptions import TransportQueryError
from os.path import join

def retrieve_page_by_id(self, id:int):
    query = gql(
        """
        query getPageById($id:Int!){
            pages{
                single(id:$id){
                    title,
                    description, 
                    content, 
                    tags{
                        id,
                        tag,
                        title,
                    }, 
                    hash 
                
                }
            }
        }
        """
    )
    
    params = {"id": id}

    # Execute the query on the transport
    result, err = self.query_graphql(query, params)

    try: 
        title = result['pages']['single']['title']
        description = result['pages']['single']['description']
        content = result['pages']['single']['content']
        tag = result['pages']['single']['tags']
        hash = result['pages']['single']['hash']
        err = None

    except (KeyError, TypeError): 
        title = None
        description = None
        content = None
        tag = None
        hash = None

    return title, description, content, tag, hash, err

def save_cheatsheet(self, title, description, content): 
    filename = title.replace(" ", "_") + ".md"
    with open(join(self.cheatsheet_path, filename), 'w') as cheatsheet: 
        cheatsheet.write(content)



def get_page_id_by_tags(self, tags:list): 
    query = gql(
        """
        query GetPageIdByTags($tags:[String!]){
            pages{
                list(tags:$tags){
                    title,
                    description, 
                    id, 
                    path, 
                    tags
                }
            }
        }
        """
    )

    params = {"tags": tags}

    result, err = self.query_graphql(query, params)

    if result is not None: 
        lst_tag = result['pages']['list']
        
    else: 
        lst_tag = []
    
    return lst_tag


def get_all_pages(self):
    query = gql(
        """
        query {
            pages{
                list{
                    title,
                    description, 
                    id, 
                    path, 
                    tags
                }
            }
        }
        """
    )

    result, err = self.query_graphql(query)

    if result is not None:
        lst_tag = result['pages']['list']

    else:
        lst_tag = []

    return lst_tag