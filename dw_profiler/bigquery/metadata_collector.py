from google.cloud import bigquery 
from google.cloud.bigquery.dataset import Dataset
from google.oauth2 import service_account

class BQMetadataCollector:
    def __init__(self, warehouse_name: str, credentials: str, region: str):
        self.warehouse_name = warehouse_name 
        self.credentials = service_account.Credentials.from_service_account_file(credentials) 
        self.region = region 
        self.client = bigquery.Client(
            project=self.warehouse_name,
            credentials=self.credentials
        )

    def get_dataset_metadata(self, dataset: str):
        ## adapt to query information schema
        ds_ref = self.client.dataset(dataset)
        ds = Dataset(ds_ref)
        return ds.to_api_repr()
        
