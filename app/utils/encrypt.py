import bcrypt

def encrypt(password):
    encoded_password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt());

    return hashed_password

def validate(password, hash):
    check_password = password.encode('utf-8')
    hashed_password = hash.encode('utf-8')
    
    return bcrypt.checkpw(check_password, hashed_password)
