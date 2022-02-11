
import datetime
from flask import jsonify, request
from app.config import app
import jwt


def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic Auth="Login required"'}), 401
    
    user = ""

    token = jwt.encode({'username': '', 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)}, app.config['SECRET_KEY'])

    return jsonify({'message': 'Validated successfully', 'token': token.decode('UTF-8'), 
                    'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})