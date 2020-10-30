import json, requests


def copy_check():

    hdr = {'Authorization': 'Bearer eyJraWQiOiJ1cy13ZXN0LTIxIiwidHlwIjoiSldTIiwiYWxnIjoiUlM1MTIifQ.eyJzdWIiOiJ1cy13ZXN0LTI6YjFjYTgyYTktYjIzYy00YzA2LThkZjctN2YwM2I4ODFhYTRmIiwiYXVkIjoidXMtd2VzdC0yOjJlNzdjM2JkLTYyMDQtNDEwMi1hNTI0LTRmYmJjYTRkZmY4NiIsImFtciI6WyJhdXRoZW50aWNhdGVkIiwiY29nbml0by1pZHAudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20vdXMtd2VzdC0yX3F2bXVQYzR2WSIsImNvZ25pdG8taWRwLnVzLXdlc3QtMi5hbWF6b25hd3MuY29tL3VzLXdlc3QtMl9xdm11UGM0dlk6Q29nbml0b1NpZ25Jbjo3ZTVkNTE3Zi1kNzE1LTRkOGUtOGYwZS0yYWEzNzIzZmJmZjIiXSwiaXNzIjoiaHR0cHM6Ly9jb2duaXRvLWlkZW50aXR5LmFtYXpvbmF3cy5jb20iLCJleHAiOjE1ODg4Njc1NzIsImlhdCI6MTU4ODg2Njk3Mn0.U9ha69GObYa0sMwByFh4x2C3g4Tgpcs7I-Co47R66DAHrATNUjTZ2tc_U9S2JoA_9ZBzR2ty_GWDSaF0_OOfHS4AdYWF8eZhdBEhbmMXyQk1g6TVb9eF7Gx99Tz1-j1X_cxX-P_y15AaQL1RtHS0tZSZJOctsXSVt_FMkqgEr1AM_ERP9ROivFvMleuDfkrBBz9jAXXgVOuLcNfENaOpF31C4RG8KUd47cwStj2Fo6BxSyq-6hd4RiFkKWJpZuMVZgJN7A-SWF4NrtwyMw_m4kRKhzfCj0HI4KrVgavxHLBFjSKvyuKV2U5rytDMco0AbkUgxlVEXXP8ixzBkeXEdw',
           'Content-Type': 'application/json'}


    data = {"orgId": "949164ee-f216-46e5-be8f-e91f0bb85f62",
        'collections':  [{
            "collectionId": "0dd1dce7-75ae-4406-8e64-4a15df13a780",
            "collection": "true",
            "annotation": "true",
            "zipCollection": "false"
        }]}
    # Call copy API
    required_params_list = ['collectionName', 'collectionId', 'collectionDownloadUrl',
                            'annotationDownloadUrl', 'maskUrl']
    copy_response = requests.post(url='https://apps.test.us-west-2.edison.gehealthcloud.io/eai_tsdcsapi/v1/collection-export',
                                  headers=hdr,
                                  data=json.dumps(data))

    jsonified_copy_response = copy_response.json()
    print(jsonified_copy_response)
    annotation_url_list = []
    mask_url_list = []
    collection_info = []
    collection_ids = []
    for collections in jsonified_copy_response.get('response'):
        collection_info.append({k: v for k, v in collections.items() if k in required_params_list})

    print(" The collection info is ", collection_info)

    for collection in collection_info:
        # collection_ids.append([v for k, v in collection.items() if k == 'collectionId'])
        for k, v in collection.items():
            if k == "collectionId":
                collection_ids.append(v)
            elif k == "annotationDownloadUrl":
                annotation_url_list.append(v)
            elif k == "maskUrl":
                mask_url_list.append(v)


    #print(" The annotation url is ", annotation_url_list)
    #print(" The mask url is ", mask_url_list)



copy_check()