import jwt
import datetime
import os
from flask import jsonify, request
from .user_model import users, User
from App import app


from ..utilities.utility import SECRET_KEY, check_for_token


@app.route("/api/v1/users", methods=['POST'])
def create_user():
    request_data = request.get_json()
    usernname = request_data["username"]
    email = request_data["email"]
    password = request_data["password"]
    new_user = User(username=usernname, password=password,
                    email=email).to_dict()
    users.append(new_user)
    return jsonify({
        "message": "user was created successfully",
        "user": new_user
    }), 201


@app.route("/api/v1/users/login", methods=['POST'])
def login_user():
    request_data = request.get_json()
    username = request_data["username"]
    password = request_data["password"]

    for user in users:
        if user["username"] == username and user["password"] == password:
            token = jwt.encode({
                "user": username,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=40)
            }, SECRET_KEY)

    return jsonify({
        "message": "user loggedin successfully",
        "token": token
    }), 200
