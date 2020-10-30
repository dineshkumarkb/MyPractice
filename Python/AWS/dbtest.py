
#import requests,json

import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

def get_dynamo_table():
    """
    :return:
    """
    try:
        dynamodb = boto3.resource('dynamodb', region_name = 'us-west-2')
        response = dynamodb.Table("test-eai-ts-notebooktable")
        return response
    except ClientError as e:
        response = e.args
        return False



collections_list = []

def get_collection_metadata():
    """
    :return:
    """
    #dynamodb = boto3.resource('dynamodb',region_name='us-west-2')
    #table = dynamodb.Table('test-eai-ts-notebooktable')

    db_elements = get_dynamo_table().scan(
        FilterExpression=Key('InstanceId').eq('510fb966-f4e3-404b-bf4a-ca3233b250c5')
    )

    print(db_elements)

    for item in db_elements.get('Items'):
        for metadata in item.get("CollectionMetadata"):
            if metadata.get("collectionDownloadUrl") not in collections_list:
                collections_list.append(metadata.get("collectionDownloadUrl"))

    print(collections_list)


op = get_collection_metadata()
