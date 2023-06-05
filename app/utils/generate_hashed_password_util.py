import os, hashlib, binascii


def hash_password(password):
    salt = hashlib.sha256(os.urandom(64)).hexdigest().encode('ascii')
    password_hash = hashlib.pbkdf2_hmac('sha256',password.encode('utf-8'),
    salt, 100000)
    password_hash = binascii.hexlify(password_hash)
    return (salt+password_hash).decode('ascii')



