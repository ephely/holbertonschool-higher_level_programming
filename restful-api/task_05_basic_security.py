"""Flask API with Basic Auth and JWT"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, get_jwt_identity,
    jwt_required
)

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'azerty(really-good-password)'
jwt = JWTManager(app)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify Basic Auth credentials"""
    if username in users and check_password_hash(users[username]["password"],
                                                 password):
        return username
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Basic Auth protected route"""
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """Generate JWT token on login"""
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 401

    if username not in users or not check_password_hash(
        users[username]["password"], password
    ):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]["role"]}
    )
    return jsonify({"access_token": access_token})


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """JWT-protected route"""
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Admin-only route"""
    current_user = get_jwt_identity()
    if users[current_user]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing/invalid token"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(header, payload):
    """Handle expired token"""
    return jsonify({"error": "Token has expired"}), 401


if __name__ == '__main__':
    app.run(port=5000)
