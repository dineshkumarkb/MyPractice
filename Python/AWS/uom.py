#import requests
from botocore.vendored import requests

class SM_Client(object):
    """
    A class to return SM client object
    """
    _sm_client = None
    uom_header = {
        'Content-Type': 'application/json'
    }




def get_user_roles(header):
    """
    :param header: Request headers
    :return: UOM response
    """


    url = 'https://core.prdge.us-west-2.eng.gehealthcloud.io/idam_uomapi/v2/user/me?detailed=true&orgrole=false'
    SM_Client.uom_header['Authorization'] = header['Authorization']
    print(" The uom_header is ",SM_Client.uom_header)
    # UOM call requires content type to be set.It does not accept non null get requests
    json_response = requests.get(url, headers=SM_Client.uom_header).json()
    # json_response = None

    # Get all roles for the current user
    roles_list = []
    user_org = None
    print(" The json response is ", json_response)
    for entity in json_response.get('userEntityAppRoles'):
        # Entity name should be Edison AI.
        if entity['entityName'] == 'Edison AI':
            # Get user roles and corresponding orgId
            roles = entity['roles']
            user_org = entity['parentOrganization']['id']
            # Get all available roles for the current user
            for role in roles:
                roles_list.append(role['code'])
    resp = {'roles': roles_list, 'user_org': user_org }
    resp['user_id'] = '{0} {1}'.format(json_response['givenName'], json_response['familyName'])

    return resp


headers = {
    'Content-Type': 'application/json',
    'Authorization' : 'Bearer eyJraWQiOiJ1cy13ZXN0LTIxIiwidHlwIjoiSldTIiwiYWxnIjoiUlM1MTIifQ.eyJzdWIiOiJ1cy13ZXN0LTI6MDhjMTVjNjgtM2M0NC00NmYzLWFlY2UtYWQ5YzA1NjViN2UwIiwiYXVkIjoidXMtd2VzdC0yOjJlYzk4YTczLWNiYjEtNGI1My04YzE5LTFlOGRlNDk5M2QwMiIsImFtciI6WyJhdXRoZW50aWNhdGVkIiwiY29nbml0by1pZHAudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20vdXMtd2VzdC0yX0xySmFpRXhRcSIsImNvZ25pdG8taWRwLnVzLXdlc3QtMi5hbWF6b25hd3MuY29tL3VzLXdlc3QtMl9MckphaUV4UXE6Q29nbml0b1NpZ25JbjpkN2JmOGYwYS1mZTU4LTRmNzItYmVkNi01MGEyYjE1NTZhNWUiXSwiaXNzIjoiaHR0cHM6Ly9jb2duaXRvLWlkZW50aXR5LmFtYXpvbmF3cy5jb20iLCJleHAiOjE1Nzg0NjA3NjksImlhdCI6MTU3ODQ2MDE2OX0.XwX6Bri2Z2DJkQFOF8owe0bjEK-FeimuvFweACcUSAg0Zy_SGmoSvssbTX5uteTWeDeNTLsPC6ZMpczzEfotIWc_y79hovINfxUGqe_ELfV8zBjrwgVPdSnnwsTU15gcUWi2X2ThQ_wjXF8BXPeHVxLS-XKLyuq2UPe-OOpjZGVwcaKu1VThx8XlJhFGKpJt30b0Mu1myuXeeaP57elNjAcSBZV31odJqj1FfoRGCusQK95etzJN34JA0SPmHM05VOr1St6WlBQW-K0FAccbgOqZyGVY3i94Sb9ajo94EVNxk8MiJHMkg7pzsvu-l1Ao_4PnbDxNJ9M7FXUeAKvqTg'
}
get_user_roles(header=headers)