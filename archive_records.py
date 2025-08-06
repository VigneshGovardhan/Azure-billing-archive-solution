import datetime, json
from azure.cosmos import CosmosClient
from azure.storage.blob import BlobServiceClient

def archive_old_billing_records():
    cosmos = CosmosClient("<COSMOS-URI>", "<COSMOS-KEY>")
    container = cosmos.get_database_client("<DB>").get_container_client("<CONTAINER>")
    blob_service = BlobServiceClient.from_connection_string("<BLOB_CONN_STR>")
    cutoff_date = (datetime.datetime.utcnow() - datetime.timedelta(days=90)).isoformat()

    query = "SELECT * FROM c WHERE c.timestamp < @cutoff"
    for item in container.query_items(query, parameters=[{'name': '@cutoff', 'value': cutoff_date}]):
        record_id = item['id']
        blob = blob_service.get_blob_client(container="billing-archive", blob=f"{record_id}.json")
        blob.upload_blob(json.dumps(item), overwrite=True)
        container.delete_item(item, partition_key=item['partitionKey'])
