
import datetime
from app.utils.encrypt import validate
from flask import jsonify, make_response, request
from app.config import app
import jwt

from app.src.services.user_services import get_by_username


def auth(username, password):
    if not username or not password:
        return make_response(jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic Auth="Login required"'}), 401)
    
    user = get_by_username(username)

    if not user:
        return make_response(jsonify({'message': 'User not found'}), 403)

    if user and validate(password, user["password"]):
        token = jwt.encode({'username': user["username"], 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)}, app.config['SECRET_KEY'])
        
        return jsonify({'message': 'Validated successfully', 'token': token, 
                    'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})

    return make_response(jsonify({'message': 'Could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 403)