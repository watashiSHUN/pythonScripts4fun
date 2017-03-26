from azure.storage.blob import BlockBlobService
import base64 # for block id
import types

def BlobBlockListToStr(self):
    # return str
    returnV = ['committed_blocks:']
    for blobblock in self.committed_blocks:
        returnV.append("\tid:{0}, state:{1}, size:{2}".format(blobblock.id,blobblock.state,blobblock.size))
    returnV.append('uncommitted_blocks:')
    for blobblock in self.uncommitted_blocks:
        returnV.append("\tid:{0}, state:{1}, size:{2}".format(blobblock.id,blobblock.state,blobblock.size))
    return "\n".join(returnV)

block_blob_service = BlockBlobService(account_name='shunstoragetest', account_key='')
# block blob service, created a connection to azure...that's yet
# self of block-blob-service has _get_host_location()

generator = block_blob_service.list_blobs('shuntestcontainer')
for blob in generator:
    print(blob.name)
blob_block_list = block_blob_service.get_block_list('shuntestcontainer','findsubstring.py',block_list_type='all')
print(blob_block_list.__str__)
blob_block_list.__class__.__str__ = BlobBlockListToStr
print(blob_block_list)
#blob_block_list.__str__ = types.MethodType(BlobBlockListToStr,blob_block_list)
#blob_block_list.__repr__ = types.MethodType(BlobBlockListToStr,blob_block_list)
#print(blob_block_list.__str__)
#print(str(blob_block_list))
#print(blob_block_list.__str__())
# print(blob_block_list.committed_blocks) # empyt list?
# print(blob_block_list.uncommitted_blocks)

with open('C:\\Users\\shucai\\Desktop\\blockblobs.txt') as output:
    blockid = base64.b64encode(b'shun test block id 1')
    block_blob_service.put_block('shuntestcontainer',
                                'findsubstring.py', # name of the existing block
                                output,
                                blockid)
# write to the block blob (multiple blobs?)
