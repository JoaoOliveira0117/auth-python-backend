import bcrypt

def encrypt(password):
    encoded_password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt());

    return hashed_password

def validate(password):
    check_password = password.encode('utf-8')
    #hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt(10));
