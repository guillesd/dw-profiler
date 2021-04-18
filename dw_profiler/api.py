

class Api:
    """ 
    This class will serve as a common interface for the different warehouses
    that could be profiled.
    """
    
    def __init__(self, warehouse_type: str, warehouse_name: str, credentials: str=None, region: str=None):
        if warehouse_type == 'bigquery':
            if credentials == None:
                raise Exception("Missing credentials")
            else:
                pass
        
        else: 
            raise Exception("Unsupported data warehouse")
