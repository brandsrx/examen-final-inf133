from app.database import db

class Restaruantes(db.Model):
    __tablename___ = "restaruantes"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=True)
    address = db.Column(db.String,nullable=True)
    city = db.Column(db.String,nullable=True)
    phone = db.Column(db.String,nullable=True)
    description = db.Column(db.String,nullable=True)
    rating = db.Column(db.Double,nullable=True)
    
    def __init__(self,name,address,city,phone,description,rating):
        self.name = name
        self.address = address
        self.city = city
        self.phone = phone
        self.description = description
        self.rating = rating

        
    def save(self):
        db.session.add(self)
        db.session.commit()
    @staticmethod
    def get_all():
        return Restaruantes.query.all()
    @staticmethod
    def get_by_id(id):
        return Restaruantes.query.get(id)
    
    def update(self,name=None,address=None,city=None,phone=None,description=None,rating=None):
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if city is not None:
            self.city = city
        if phone is not None:
            self.phone = phone
        if description is not None:
            self.description = description
        if rating is not None:
            self.rating = rating
        db.session.commit()
            
    def delete(self):
        db.session.delete(self)
        db.session.commit()