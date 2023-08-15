import jwt

def decode_uuid_from_jwt(token: str) -> str:
    uuid = token.split("Token ")[1]
    decoded_data = jwt.decode(
        uuid, 
        os.environ.get("SECRET_KEY"),
        algorithms=['HS256']
    )

    return decoded_data["user_uuid"]