from azure.storage.blob import BlockBlobService
block_blob_service = BlockBlobService(account_name='shunstoragetest', account_key='')
generator = block_blob_service.list_blobs('shuntestcontainer')
for blob in generator:
    print(blob.name)
