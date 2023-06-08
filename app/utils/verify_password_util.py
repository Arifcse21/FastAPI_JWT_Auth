import hashlib, binascii


def verify_password(password, hashed_password):
    # Extract the salt and stored password hash from the hashed password
    salt = hashed_password[:64].encode('ascii')
    stored_password_hash = hashed_password[64:]
    
    # Hash the provided password with the extracted salt
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    password_hash = binascii.hexlify(password_hash).decode('ascii')
    
    # Compare the stored password hash with the computed password hash
    return password_hash == stored_password_hash
