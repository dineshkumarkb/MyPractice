import boto3
import requests
from requests_aws4auth import AWS4Auth

host = 'https://vpc-dev-eai-wui-domain-cow6xmllnxjrish3jn2sb2vobe.us-west-2.es.amazonaws.com'
region = 'us-west-2'  # For example, us-west-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

# Register repository
path = '_snapshot/dev-es-snapshot'  # the Elasticsearch API endpoint
url = host + path

payload = {
    "type": "s3",
    "settings": {
        "bucket": "dev-eai-es-snapshot",
        "region": "us-west-2",
        "role_arn": "arn:aws:iam::551934631674:role/Es-Snapshot-ESSnapshotRole-1X49HBSLVG2DU"
    }
}

headers = {"Content-Type": "application/json"}

r = requests.put(url, auth=awsauth, json=payload, headers=headers, timeout)

print(r.status_code)
print(r.text)