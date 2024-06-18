from app.database import db
from werkzeug.security import generate_password_hash
from flask_login import UserMixin

class Usuarios(UserMixin,db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,unique=True,nullable=True)
    email = db.Column(db.String,unique=True,nullable=True)
    phone = db.Column(db.String,unique=True,nullable=True)
    password_hash = db.Column(db.String,nullable=True)
    role = db.Column(db.String,nullable=True)
    
    def __init__(self,name,email,phone,password,role=["customer"]):
        self.name = name
        self.email = email
        self.phone = phone
        self.set_password(password)
        self.role = role
        
    def save(self):
        db.session.add(self)
        db.session.commit()
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    @staticmethod
    def get_by_id(id):
        return Usuarios.query.get(id)
    @staticmethod
    def find_by_useremail(email):
        return Usuarios.query.filter_by(email=email).first()

    def has_role(self,role):
        return self.role == role
    
    