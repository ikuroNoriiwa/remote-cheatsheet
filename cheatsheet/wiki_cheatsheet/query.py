from gql import gql
from gql.transport.exceptions import TransportQueryError

def query_graphql(self, gql_query, params=None): 
    """
    """
    try: 
        if params is not None: 
            result = self.client.execute(gql_query, variable_values=params)
            err = None
        else: 
            result = self.client.execute(gql_query)
            err = None

    except TransportQueryError as er:
        err = er.errors[0]['message']
        result = None

    return result, err 