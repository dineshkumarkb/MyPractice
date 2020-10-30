import boto3
#from awsretry import AWSRetry
from botocore.config import Config

from multiprocessing import Process,current_process



def create_service():


    conf = Config(retries = dict(max_attempts = 10))
    client = boto3.client('sagemaker')
    count = 1
    #for i in range(200):
    print(" The response is {} by process {} ".format(client.list_notebook_instances(),current_process().name))
    #    count+=1



if __name__ == "__main__":
    for i in range(200):
        mul_proc = Process(target=create_service)
        mul_proc.start()


#create_service()




