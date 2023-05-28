import datetime
import jwt
import os
from typing import Dict


class AccessTokenUtil:
    """
    Access token generator util class
    """
    @staticmethod
    def generate_access_token(uuid: str):
        """
        Generate access token against user uuid
        :param uuid: user uuid
        """
        print('user uuid = ', str(uuid))
        access_token_payload = {
            'user_id': str(uuid),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7, minutes=5),
            'iat': datetime.datetime.utcnow(),
        }
        access_token = jwt.encode(
            access_token_payload,
            key=os.environ.get("SECRET_KEY"),
            algorithm=os.environ.get("ALGORITHM")
        )
        return access_token
