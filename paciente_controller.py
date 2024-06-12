from flask import flash,redirect,url_for,Blueprint,request
from models.pacientes_models import Pacientes
from flask_login import login_required
from views import pacientes_view
from utils.decorators import role_required
from datetime import datetime
pac_bp = Blueprint("paciente",__name__)


@pac_bp.route("/patients",methods=["GET"])
@login_required
@role_required("admin")
def list_pacientes():
    paci = Pacientes.get_all()
    return pacientes_view.list_pacientes(pacientes=paci)

@pac_bp.route("/patients/create",methods=["GET","POST"])
@login_required
@role_required("admin")
def create_pacientes():
    if request.method == "POST":
        name = request.form["name"]
        lastname = request.form["apellidos"]
        ci = request.form["age"]
        bisrt_date = request.form["birth_date"]
        date_obj = datetime.strptime(bisrt_date, '%Y-%m-%d').date()
        pac = Pacientes(name,lastname,ci,date_obj)
        pac.save()
        flash("Se registro correctamene")
        return redirect(url_for("paciente.list_pacientes"))
    return pacientes_view.create_pacientes()
@pac_bp.route("/patients/<int:id>/update",methods=["GET","POST"])
@login_required
@role_required("admin")
def update_patients(id):
    paci = Pacientes.get_by_id(id)
    if request.method == "POST":
        name = request.form["name"]
        lastname = request.form["lastname"]
        ci = request.form["ci"]
        bisrt_date = request.form["birth_date"]
        date_obj = datetime.strptime(bisrt_date, '%Y-%m-%d').date()
        paci.update(name,lastname,ci,date_obj)
        flash("Paciente actualizado")
        return redirect(url_for("paciente.list_pacientes"))
    return pacientes_view.update_paciente(paci)

@pac_bp.route("/patients/<int:id>/delete",methods=["GET"])
@login_required
@role_required("admin")
def delete_patient(id):
    paci = Pacientes.get_by_id(id)
    paci.delete()
    flash("Se elimino correctamente")
    return redirect(url_for("paciente.list_pacientes"))