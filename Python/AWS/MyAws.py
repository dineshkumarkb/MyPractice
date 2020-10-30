# from boto.s3.connection import S3Connection
#
# conn = S3Connection()
# mybucket = conn.get_bucket('dkbtesting')
#
#
# for i in mybucket.get_all_keys():
#     print i.key


# import boto3
#
# s3 = boto3.client('s3',aws_access_key_id="AKIAVGBDWGVJHKA6NIRE",
#                   aws_secret_access_key = "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"
#                   )
#
# s3.download_file('dkbtesting',
#                  'Dinesh.jpg','D:\Learning_Repo\dinesh\Python\AWS\Dinesh_mod.jpg')


# import boto3
#
# session = boto3.session.Session(aws_access_key_id='AKIAVGBDWGVJHKA6NIRE',
#                                 aws_secret_access_key='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'
#                                 )
#
# s3 = session.resource('s3')


# import boto3
#
# client = boto3.client('sagemaker')
#
# my_resp =  client.list_notebook_instances()['NotebookInstances']
#
# #my_desc = client.describe_notebook_instance(NotebookInstanceName = 'sotefs1')
#
#
#
# print (my_resp)
# #print(my_desc)


# import boto3
#
# client = boto3.client('comprehendmedical')
#
# result = client.detect_entities(Text= 'cerealx 84 mg daily')
# print(result)
# entities = result['Entities']
# for entity in entities:
#     print('Entity', entity)




# def test_mem(ele,l=[]):
#
#     l.append(ele)
#
#     print(l)
#
# test_mem(ele=1)
# test_mem(ele=2)
# test_mem(ele=3)
# test_mem(ele=4)

# import sqlalchemy as db
# import pandas as pd
#
# conn = db.create_engine("sqlite:///D:\\Learning_Repo\\dinesh\\Python\\AWS\\namedb.db",echo=True)
#
# df = pd.read_csv(r'C:\Users\212757215\Desktop\StaffMember.csv')
#
# print(df.head())
#
# df[["abbreviation","personid"]].to_sql('patients',con=conn,if_exists="append",index=False)
#
# print(conn.execute("SELECT * FROM patients").fetchall())
#
# import os
# print((os.path.dirname(os.path.abspath(__file__))))
#print(os.path.basename(__file__))



# import requests
#
#
# headers = {"Content-Type":"application/json",
# "Authorization":"Bearer eyJraWQiOiJ1cy13ZXN0LTIxIiwidHlwIjoiSldTIiwiYWxnIjoiUlM1MTIifQ.eyJzdWIiOiJ1cy13ZXN0LTI6NGNjYjMyNWYtNDlhYi00YmQ1LWFmY2QtYWE4ODhkZDY3OWYxIiwiYXVkIjoidXMtd2VzdC0yOjJlNzdjM2JkLTYyMDQtNDEwMi1hNTI0LTRmYmJjYTRkZmY4NiIsImFtciI6WyJhdXRoZW50aWNhdGVkIiwiY29nbml0by1pZHAudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20vdXMtd2VzdC0yX3F2bXVQYzR2WSIsImNvZ25pdG8taWRwLnVzLXdlc3QtMi5hbWF6b25hd3MuY29tL3VzLXdlc3QtMl9xdm11UGM0dlk6Q29nbml0b1NpZ25JbjpjY2FjZDM0Ny0yZjA3LTRiNzYtOGIwOC03NmIwYWY5MDhkYjQiXSwiaXNzIjoiaHR0cHM6Ly9jb2duaXRvLWlkZW50aXR5LmFtYXpvbmF3cy5jb20iLCJleHAiOjE1NzU1NTMyMzQsImlhdCI6MTU3NTU1MjYzNH0.Mls02Ql9-Tyh0lH4z1935W7TXx3kqWgpk4KNA1PmTE2M11r7A__m0DkT4hZbdHldDj7wkQbk3VvkO0p6bHjlwAerwGODPGCJ-J070eMlROqi3lbLoqoPf3wpKBNBx2LKM3NrFm1h0jGDoC8Xu9UVbufM4_tmAj_zKvO8HYGdkyymsnnEfFf42YuPpD935IwRiB2BVXoN6ZDa3z8gsfvfqCTjPFDtr08Iv1cHlzTlMTVbxHpsFF-phicMM8sS1_xF1IbiO4V33D4oea-zSObTnIHSj0j9tF7Jm_mDL81AJYADlo3COA4dlhFOgD4G4codFrbkXMa3MZQztCvoVHoiiQ"}
# r = requests.get(url='https://l9rxfkv6u0.execute-api.us-west-2.amazonaws.com/test/v1/82709dd1-8924-481c-9d93-14a9e2e0c524/instancetypes',
#              headers=headers)
#
# print(r.json())

import boto3
from botocore.config import Config

# class SM_Client(object):
#     """
#     A class to return SM client object
#     """
#     _sm_client = None
#
#     @staticmethod
#     def get_sagemaker_client():
#         """
#              :return: sagemaker client object
#              """
#         # Increase the number of retries to 6 to avoid ThrottlingException(default=4)
#         retry_config = Config(retries=dict(max_attempts=6))
#         if not SM_Client._sm_client:
#             SM_Client._sm_client = boto3.client('sagemaker', config=retry_config)
#         return SM_Client._sm_client
#
#
#
# SM_Client.get_sagemaker_client()

import  logging
import boto3
from botocore.exceptions import ClientError
import datetime
LOG = logging.getLogger("MyAws")
LOG_FILE = "MyAws: "
#logging.basicConfig(level=logging.INFO)

from boto3.dynamodb.conditions import Key, Attr
table = boto3.resource('dynamodb',region_name = 'us-west-2').Table('dev-eai-notebooktable')

primary_key = {
    'OrgId': '82709dd1-8924-481c-9d93-14a9e2e0c524',
    'InstanceName':'refactor5'
}




def query_failed_instances():

    response = table.scan(FilterExpression=Key('InstanceStatus').eq('Failed') | Key('InstanceStatus').eq('FAILED'))
    print(response['Items'])
    # for item in response['Items']:
    #     if item['InstanceStatus'].capitalize() == 'Failed':
    #         primary_key['InstanceName'] = item['InstanceName']
    #         resp = table.delete_item(Key={
    #
    #             'OrgId':item['OrgId'],
    #             'InstanceName': item['InstanceName']
    #
    #         })
    #         print(resp)


#query_failed_instances()

#
# def query_notebook_state(table_name,primary_key):
#     """
#     :param instance_name: Instance name of the state to be checked
#     :return: state
#     """
#
#     LOG.info("deleting entry with ID: {0} from table {1}".format(primary_key, table_name))
#     table = boto3.resource('dynamodb', region_name='us-west-2').Table('dev-eai-notebooktable')
#
#     resp = table.get_item(Key=primary_key)
#     LOG.debug(LOG_FILE + " The deleted response is ", str(resp))
#
#     print(resp['Item'])
#
#
# query_notebook_state('dev-eai-notebooktable',primary_key)


# class NotebookError(Exception):
#     pass
#
#     # def __init__(self,message):
#     #     super(NotebookError, self).__init__(message)
#     #     self.message=" Notebook does not exist "
#
#
# raise NotebookError(400,{"errors":["TestError"]})

import boto3
from timeloop import Timeloop
from datetime import timedelta

sm = boto3.client('sagemaker',region_name="us-west-2")

t1= Timeloop()

data = {
	"collectionIds": [
		"b70ea2f9-4dab-4c15-bacf-648660dfd0c7"
		],
		"orgId": "82709dd1-8924-481c-9d93-14a9e2e0c524"
}



import requests,json
headers = {"Content-Type":"application/json",
"Authorization":"Bearer eyJraWQiOiJ1cy13ZXN0LTIxIiwidHlwIjoiSldTIiwiYWxnIjoiUlM1MTIifQ.eyJzdWIiOiJ1cy13ZXN0LTI6NGNjYjMyNWYtNDlhYi00YmQ1LWFmY2QtYWE4ODhkZDY3OWYxIiwiYXVkIjoidXMtd2VzdC0yOjJlNzdjM2JkLTYyMDQtNDEwMi1hNTI0LTRmYmJjYTRkZmY4NiIsImFtciI6WyJhdXRoZW50aWNhdGVkIiwiY29nbml0by1pZHAudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20vdXMtd2VzdC0yX3F2bXVQYzR2WSIsImNvZ25pdG8taWRwLnVzLXdlc3QtMi5hbWF6b25hd3MuY29tL3VzLXdlc3QtMl9xdm11UGM0dlk6Q29nbml0b1NpZ25JbjpjY2FjZDM0Ny0yZjA3LTRiNzYtOGIwOC03NmIwYWY5MDhkYjQiXSwiaXNzIjoiaHR0cHM6Ly9jb2duaXRvLWlkZW50aXR5LmFtYXpvbmF3cy5jb20iLCJleHAiOjE1NzY0Mjg4OTIsImlhdCI6MTU3NjQyODI5Mn0.ZRpiDWsXqeYgTPamacOMUtXDp8qsqSE2QX5RAqH2ZCr3Sy0RTSHotSXoyrKZiN1YRagrFS7u7QG8_hMUeWA5QVG2oMBL4pqfF_vJ34R9hVz3akR9tJ7f92LVpmD5NgmVMRUvgjQp_3v3sp2lmF812VP_CvvAXO0zu0YSkTCsvjHqJtaVybDeh0t-Gpao9W8wXF0meIFJQG9JkW_szCvTbvFCGJ9j4UzWpUpOLJUBJJJsci-wmHCX8bsWPAfBfmDcerGAbBfBRXzEe8uIxKPwaPUwMlf_gM5x_kZ0xB0Fy8yb__rJD919gSig03c75XsY2mnqq0kk7juM-xm7674KPw"}




#@t1.job(interval=timedelta(seconds=5))
def list_notebooks():
    print(" Inside list ")
    #list = sm.list_notebook_instances(MaxResults=100,SortBy='Name')
    #print(" Inside list notebooks ", list)

    r = requests.post(
        url='https://htnqwf8003.execute-api.us-west-2.amazonaws.com/dev_eai_tsdcsapi1/v1/collection-export/status/collections',
        headers=headers,
        data=json.dumps(data))
    print(r.json().get('status'))
    #return r.json().get('status')[0]['collectionStatus']

#list_notebooks()

#t1.start()

def another_method():
    print(" Another method ")

another_method()


import threading
from threading import Timer,Event
myevent = Event()
t = threading.Thread(target=list_notebooks)
t.setName("Thread1")
#t.start()
#t.join()





# import multitimer
#
#
# timer =multitimer.MultiTimer(interval=10,function=list_notebooks)
# timer.start()






# from polling import TimeoutException, poll
#
# poll(lambda : requests.post(
#         url='https://htnqwf8003.execute-api.us-west-2.amazonaws.com/dev_eai_tsdcsapi1/v1/collection-export/status/collections',
#         headers=headers,
#         data=json.dumps(data)).json().get('status')[0]['collectionStatus'] == 'COMPLETED',step=1,max_tries=2)




