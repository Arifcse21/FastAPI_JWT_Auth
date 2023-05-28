import datetime
import jwt
import os


class RefreshTokenUtil:
    """
    Generates refresh token util class
    """
    @staticmethod
    def generate_refresh_token(uuid: str):
        """
        Generates refresh token against user uuid
        :param uuid: user uuid
        """
        refresh_token_payload = {
            'user_id': str(uuid),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
            'iat': datetime.datetime.utcnow()
        }
        refresh_token = jwt.encode(
            refresh_token_payload,
            key=os.environ.get("SECRET_KEY"),
            algorithm='HS256'
        )

        return refresh_token
