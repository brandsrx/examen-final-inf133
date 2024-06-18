from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

from app.models.usuarios_models import Usuarios

user_bp = Blueprint("user", __name__)
@user_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    password = data.get("password")
    roles = data.get("role")

    if not name or not email or not phone or not phone or not password:
        return jsonify({"error": "Se requieren nombre de usuario y contraseña"}), 400

    existing_user = Usuarios.find_by_useremail(email)
    if existing_user:
        return jsonify({"error": "El correo electrónico ya está en uso"}), 400

    new_user = Usuarios(name,email,phone, password, roles)
    new_user.save()

    return jsonify({"message": "Usuario creado exitosamente"}), 201


@user_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    useremail = data.get("email")
    password = data.get("password")
    print(data)
    user = Usuarios.find_by_useremail(useremail)
    print(user)
    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(
            identity={"username": user.name, "role": user.role}
        )
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401
