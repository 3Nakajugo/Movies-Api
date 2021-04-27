import os
import jwt
from flask import jsonify, request
from functools import wraps


SECRET_KEY = os.environ.get("SECRET_KEY")


def check_for_token(func):
    """ create authentication decorator"""
    @wraps(func)
    def wrapped(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({
                "message": "token is missing"
            }), 403
        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms="HS256")
        except jwt.InvalidSignatureError:
            return jsonify({"message": "token is invalid"}), 403
        except jwt.ExpiredSignatureError:
            return jsonify({"message": " Your token has expired"}), 403
        return func(*args, **kwargs)
    return wrapped
