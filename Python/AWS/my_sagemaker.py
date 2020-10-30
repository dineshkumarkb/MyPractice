import boto3
import time
import  base64


EFS_CREATED = False

def create_efs():
    """
    This method is to create an efs ONLY once during creation of
    the first notebook
    :return:
    """
    if not EFS_CREATED:
        efs_client = boto3.client('efs')
        response = efs_client.create_file_system(CreationToken = "testtoken",
                                             PerformanceMode = 'generalPurpose',
                                             Encrypted = False)

        file_sys_id = response['FileSystemId']
        time.sleep(10)
        mnt_resp = efs_client.create_mount_target(FileSystemId = file_sys_id,
                                       SubnetId = "subnet-0c5c8a16059dea1cb",
                                                  SecurityGroups=[
                                                      '',
                                                  ]
                                                  )

        print(response)
        print(file_sys_id)
        print(mnt_resp)


def del_efs():

    efs_client = boto3.client('efs')
    resp = efs_client.describe_file_systems()
    for clients in resp['FileSystems']:
        fsd = (clients['FileSystemId'])
        response = efs_client.delete_file_system(FileSystemId = fsd)
        print(response)

def describe():

    efs_client = boto3.client('efs')
    desc = efs_client.describe_mount_targets(FileSystemId = "fs-2d56bdfc")
    print(desc)


def mount_me():

    efs_client = boto3.client('efs')
    res = efs_client.create_mount_target(FileSystemId = "fs-2d56bdfc",
                                         SubnetId = "subnet-a9ca94c1")
    print (res)


def create_sagemaker():
    oncreate = '\nsudo yum install -y amazon-efs-utils' \
               '\nmkdir /home/ec2-user/SageMaker/efs'
    convert = bytes(oncreate, 'utf-8')
    encoded = base64.b64encode(convert)

    ipaddress = '172.31.22.74'
    onstart = '\nsudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 {}:/ /home/ec2-user/SageMaker/efs' \
              '\nsudo chmod go+rw /home/ec2-user/SageMaker/efs'.format(ipaddress)

    st_convert = bytes(onstart,'utf-8')
    st_encoded = base64.b64encode(st_convert)

    sm_client  = boto3.client('sagemaker',region_name = 'ap-south-1')
    resp = sm_client.create_notebook_instance_lifecycle_config(

        NotebookInstanceLifecycleConfigName='prgmountefs',
        OnCreate=[
            {
                'Content': encoded.decode('utf-8')
            },
        ],
        OnStart=[
            {
                'Content': st_encoded.decode('utf-8')
            },
        ]

    )

    sm_resp = sm_client.create_notebook_instance(
        NotebookInstanceName='prmnefsnotebook',
        InstanceType='ml.t2.medium',
        SecurityGroupIds=['sg-4386a229'],
        SubnetId = 'subnet-b80341d0',
        LifecycleConfigName='prgmountefs',
        RoleArn='arn:aws:iam::995118007547:role/service-role/AmazonSageMaker-ExecutionRole-20190610T114407'
    )
    print(resp)
    #print(sm_resp)




def get_vpc():

    sm_client =  boto3.client('sagemaker',region_name = 'ap-south-1')
    resp = sm_client.describe_notebook_instance(NotebookInstanceName = 'efstest1')
    print(resp)





#del_efs()
#describe()
#create_efs()
#mount_me()
#create_sagemaker()
get_vpc()