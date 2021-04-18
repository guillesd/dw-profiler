from cloud.google import bigquery 

class WHMetadataCollector:
    def __init__(self, warehouse_name: str, credentials: str, region: str):
        self.warehouse_name = warehouse_name 
        self.credentials = credentials 
        self.region = region 

    def _set_api_connection(self):
        self.client = bigquery.Client(
            project=self.warehosue_name,
            credentials=self.credentials
        )
        