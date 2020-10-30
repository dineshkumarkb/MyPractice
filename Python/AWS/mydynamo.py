import boto3
from boto3.dynamodb.conditions import Key, Attr

db_client = boto3.resource('dynamodb',region_name = "us-west-2")
table = db_client.Table('dev-eai-updated-notebook')
#
# # pk = {
# #     "InstanceId":"1",
# #     "CollectionId":"12"
# # }
# #
# # resp = table.update_item(Key=pk,UpdateExpression = "SET CollectionId = list_append(CollectionId, :i)",
# #                          ExpressionAttributeValues = {":i":[13]},ReturnValues="UPDATED_NEW")
#
# # print(resp)
#
#
# response = table.query(IndexName = 'CollectionId-index',
#                        KeyConditionExpression = Key('CollectionId').contains("12"))
#
# print(response)

COLLECTION_INDEX = "CollectionId-index"

def get_instances_for_collection(collection_id, partition_key):
    """
    :param collection_id:
    :param partition_key:
    :return:
    """

    instances_for_collections = []


    try:

        print(" Querying table for instances with collection_id and partition_key {} {} ".format(collection_id,
                                                                                                       partition_key))
        # resp = table.query(IndexName=COLLECTION_INDEX,
        #                    KeyConditionExpression=Key(partition_key).eq(collection_id),
        #                    FilterExpression=Attr('InstanceStatus').ne('EXISTING'))
        resp = table.query(IndexName=COLLECTION_INDEX,
                           KeyConditionExpression=Key("CollectionId").eq("ff742bfd-5298-49ec-9a3b-2ea771765601"),
                           FilterExpression=Attr('InstanceStatus').ne('EXISTING'))
    except Exception as e:
        resp = e.args

    print(" The table query response is {} ".format(resp))

    for i in resp['Items']:
        instances_for_collections.append(i['InstanceId'])

    print(" The instances to be returned are {} ".format(instances_for_collections))

    return instances_for_collections



get_instances_for_collection("ff742bfd-5298-49ec-9a3b-2ea771765601","CollectionId")