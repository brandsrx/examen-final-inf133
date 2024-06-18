import json
from functools import wraps

from flask import jsonify
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request


def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return fn(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": str(e)}), 401

    return wrapper


def roles_required(roles=[]):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:

                verify_jwt_in_request()
                current_user = get_jwt_identity()
                user_r = current_user.get("role",None)

                if not set(roles).intersection([user_r]):
                    return jsonify({"error": "No tiene permiso para realizar esta acción"}), 403
                return fn(*args, **kwargs)
            except Exception as e:
                print(e)
                return jsonify({"error": str(e)}), 401

        return wrapper

    return decorator
