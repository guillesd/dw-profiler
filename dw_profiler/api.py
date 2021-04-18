from bigquery.metadata_collector import BQMetadataCollector

class MetadataCollector:
    """ 
    This class will serve as a common interface for the different warehouses
    that could be profiled.
    """
    
    def __init__(self, warehouse_type: str, warehouse_name: str, credentials: str=None, region: str=None):
        if warehouse_type == 'bigquery':
            if credentials == None:
                raise Exception("Missing credentials")
            elif region = None:
                raise Exception("Rigion was not specified")
            else:
                self.metadata_collector = BQMetadataCollector(warehouse_name, credentials, region)
        
        else: 
            raise Exception("Unsupported data warehouse")
