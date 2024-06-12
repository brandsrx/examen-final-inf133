from flask import Blueprint,jsonify,request
from app.models.reservas_model import Reservas
from app.views.reservas_view import render_reserva_detail,render_reserva_list
from app.utils.decorators import jwt_required, roles_required

reservas_bp = Blueprint("reservas",__name__)

@reservas_bp.route("/reservations", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "customer"])
def get_reservations():
    reservas = Reservas.get_all()
    return jsonify(render_reserva_list(reservas)),200

@reservas_bp.route("/reservations/<int:id>",methods=["GET"])
@jwt_required
@roles_required(roles=["admin","customer"])
def get_reservation(id):
    reserva = Reservas.get_by_id(id)
    if reserva:
        return jsonify(render_reserva_detail(reserva))
    return jsonify({"error":"Reserva no encontrado"}),404

@reservas_bp.route("/reservations",methods=["POST"])
@jwt_required
@roles_required(roles=["admin","customer"])
def create_reservation():
    data = request.json
    user_id = data.get("user_id")
    restaruant_id = data.get("restaruant_id")
    reservation_date = data.get("reservation_date")
    num_guests= data.get("num_guests")
    special_requests = data.get("special_requests")
    status = data.get("status")
    
    if not user_id or not restaruant_id or not reservation_date or not num_guests or status is None:
        return jsonify({"error":"Faltan datos requeridos"}),400
    reservas = Reservas(user_id,restaruant_id,reservation_date,num_guests,special_requests,status)
    
    reservas.save()
    
    return jsonify(render_reserva_detail(reservas)),201

@reservas_bp.route("/reservations/<int:id>",methods=["PUT"])
@jwt_required
@roles_required(roles=["admin","customer"])
def update_reservations(id):
    reserva = Reservas.get_by_id(id)
    if not reserva:
        return jsonify({"error":"reserva no encontrado"}),404
    data = request.json
    user_id = data.get("user_id")
    restaruant_id = data.get("restaruant_id")
    reservation_date = data.get("reservation_date")
    num_guests= data.get("num_guests")
    special_requests = data.get("special_requests")
    status = data.get("status")
    
    try: 
        reserva.update(user_id,restaruant_id,reservation_date,num_guests,special_requests,status)
        return jsonify(render_reserva_detail(reserva)),200
    except Exception as e:
        return jsonify({"error": str(e)}), 401
    

@reservas_bp.route("/reservations/<int:id>",methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin","customer"])
def delete_reservations(id):
    reserva = Reservas.get_by_id(id)
    if not reserva:
        return jsonify({"error":"reserva no encontrado"}),404
    
    reserva.delete()
    
    return "",204
