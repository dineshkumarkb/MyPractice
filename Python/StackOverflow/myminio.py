from minio import Minio
from minio.error import SignatureDoesNotMatch, ResponseError, InvalidAccessKeyId, InvalidArgument, InvalidArgumentError

def set_user(self):
    try:
        self.user = Minio(MINIO_CONFIG['MINIO_ENDPOINT'],
                          access_key=self.username,
                          secret_key=self.password,
                          secure=MINIO_CONFIG['MINIO_SECURE'])
        return {"msg":"User is now logged in", "status": "OK"
    except SignatureDoesNotMatch as err:
        return {"msg": err.message, "status":"F"}
    except ResponseError as err:
        return {'msg': err.message, 'status': "F"}
    except InvalidAccessKeyId as err:
        return {"msg": err.message, "status":"F"}
    except InvalidArgument as err:
        return {"msg": err.message, "status":"F"}
    except InvalidArgumentError as err:
        return {"msg": err.message, "status":"F"}
