import boto3

myurl = 's3://gehc-us-west-2-039111045627-test-eai-experiment-mibdrvwn/a161e306-686b-4c1f-81c1-76521039b5bb/collection'
s3client = boto3.client('s3',region_name='us-west-2')