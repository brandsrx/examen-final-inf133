from flask import Blueprint,jsonify,request
from app.models.restaruantes_models import Restaruantes
from app.views.restaruants_view import render_restaruant_detail,render_restaruant_list
from app.utils.decorators import jwt_required, roles_required

rest_bp = Blueprint("restaruante",__name__)

@rest_bp.route("/restaurants", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "customer"])
def get_restaruantes():
    restaruantes = Restaruantes.get_all()
    return jsonify(render_restaruant_list(restaruantes)),200

@rest_bp.route("/restaurants/<int:id>",methods=["GET"])
@jwt_required
@roles_required(roles=["admin","customer"])
def get_restaruante(id):
    restaruante = Restaruantes.get_by_id(id)
    if restaruante:
        return jsonify(render_restaruant_detail(restaruante))
    return jsonify({"error":"Restaurante no encontrado"}),404

@rest_bp.route("/restaurants",methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_restaruante():
    data = request.json
    name = data.get("name")
    address = data.get("address")
    city = data.get("city")
    phone= data.get("phone")
    description = data.get("description")
    rating= data.get("rating")
    
    if not name or not description or not address or not city or not phone or rating is None:
        return jsonify({"error":"Faltan datos requeridos"}),400
    
    restaruante = Restaruantes(name=name,address=address,city=city,phone=phone,description=description,rating=rating)
    restaruante.save()
    
    return jsonify(render_restaruant_detail(restaruante)),201

@rest_bp.route("/restaurants/<int:id>",methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_restaruante(id):
    restaruante = Restaruantes.get_by_id(id)
    if not restaruante:
        return jsonify({"error":"Restaurante no encontrado"}),404
    data = request.json
    name = data.get("name")
    address = data.get("address")
    city = data.get("city")
    phone= data.get("phone")
    description = data.get("description")
    rating= data.get("rating")
    try: 
        restaruante.update(name=name,address=address,city=city,phone=phone,description=description,rating=rating)
        return jsonify(render_restaruant_detail(restaruante)),200
    except Exception as e:
        return jsonify({"error": str(e)}), 401
    

@rest_bp.route("/restaurants/<int:id>",methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_restaruante(id):
    restaruante = Restaruantes.get_by_id(id)
    if not restaruante:
        return jsonify({"error":"Restaurante no encontrado"}),404
    
    restaruante.delete()
    
    return "",204
