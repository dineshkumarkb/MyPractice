
import base64
import boto3
sm_client = boto3.client('sagemaker', region_name='us-west-2')


# create_script =  '\n sudo yum install -y amazon-efs-utils' \
#                  '\n sudo yum install -y nfs-utils' \
#                  '\n sudo mkdir -p /home/ec2-user/SageMaker/efs' \
#                  '\n sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-88fa8922.efs.us-west-2.amazonaws.com:/ /home/ec2-user/SageMaker/efs' \


# start_script = '\n sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-88fa8922.efs.us-west-2.amazonaws.com:/ /home/ec2-user/SageMaker/efs' \
#                '\n sudo chmod go+rw /home/ec2-user/SageMaker/efs'

create_script = '''sudo yum install -y amazon-efs-utils
                     sudo yum install -y nfs-utils
                     sudo mkdir -p /home/ec2-user/SageMaker/efs
                     sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-c0fec46a.efs.us-west-2.amazonaws.com:/ /home/ec2-user/SageMaker/efs'''

start_script = '''sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-c0fec46a.efs.us-west-2.amazonaws.com:/ /home/ec2-user/SageMaker/efs
                  sudo chmod go+rw /home/ec2-user/SageMaker/efs'''

create_bytes = bytes(create_script,'utf-8')
start_bytes = bytes(start_script,'utf-8')


encode_create = base64.b64encode(create_bytes)
encode_start = base64.b64encode(start_bytes)

sm_client.create_notebook_instance_lifecycle_config(NotebookInstanceLifecycleConfigName='myefs',
                                                    OnCreate=[
                                                        {
                                                            'Content': encode_create.decode("utf-8")
                                                        }
                                                    ],
                                                    OnStart=[
                                                        {
                                                            'Content': encode_start.decode('utf-8')
                                                        }
                                                    ]
                                                    )



sm_client.create_notebook_instance(NotebookInstanceName='myefs',
                                   InstanceType='ml.t2.medium',
                                   SubnetId='subnet-95794fde',
                                   SecurityGroupIds=['sg-4511510b'],
                                   LifecycleConfigName='myefs',
                                   RoleArn='arn:aws:iam::356557141330:role/MySageMakerFull')