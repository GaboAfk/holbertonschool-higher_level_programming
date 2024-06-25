#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "1234"
jwt = JWTManager(app)

users = {
      "user": {"username": "user1", "password": generate_password_hash("user"), "role": "user"},
      "admin": {"username": "admin1", "password": generate_password_hash("admin"), "role": "admin"}
  }

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify("Basic Auth: Access Granted")

# curl -X POST -H "Content-Type: application/json" -d '{"username":"user", "password": "user"}' http://127.0.0.1:5000/login

@app.route('/login', methods=["POST"])
#@jwt_required()
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if username in users and check_password_hash(users[username]["password"], password):
        acces_token = create_access_token(identity={"username": username, "role": users[username]["role"]})
        
        return jsonify({"acces_token": acces_token})

    return jsonify("Bad username or password"), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return jsonify("JWT Auth: Access Granted")

@app.route("/admin-only")
@jwt_required
def admin_only():
    current_user = get_jwt_identity()
    if current_user["role"] == "admin":
        return jsonify("Admin Access: Granted")
    else:
        return jsonify(""), 403


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run()