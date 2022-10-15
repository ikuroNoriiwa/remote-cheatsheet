from gql import gql

def get_tag_list(self): 
    # Provide a GraphQL query
    query = gql(
        """
        query{
            pages{
                list{
                tags
                }
            }
        }
    """
    )

    # Execute the query on the transport
    result = self.client.execute(query)

    list_tag = []
    for tags in result["pages"]["list"]:
        for tag in tags["tags"]: 
            if tag not in list_tag: 
                list_tag.append(tag) 
    list_tag.sort()
    return list_tag

def list_pages_with_tag(self, list_tag:list): 
    pass

