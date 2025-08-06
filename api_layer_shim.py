def get_billing_record(record_id):
    result = cosmos_db_get(record_id)
    if result:
        return result
    try:
        blob = blob_client.download_blob(f"{record_id}.json")
        return json.loads(blob.readall())
    except Exception:
        raise Exception("Record not found in both stores")
