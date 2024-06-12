from app.database import db

class Reservas(db.Model):
    __tablename___ = "reservas"
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,nullable=True)
    restaruant_id = db.Column(db.Integer,nullable=True)
    reservation_date = db.Column(db.DateTime,nullable=True)
    num_guests = db.Column(db.Integer,nullable=True)
    special_requests = db.Column(db.String,nullable=True)
    status = db.Column(db.String,nullable=True)
    def __init__(self,user_id,restaruan_id,reservation_date,num_guests,special_requests,status):
        self.user_id = user_id
        self.restaruant_id = restaruan_id
        self.reservation_date = reservation_date
        self.num_guests = num_guests
        self.special_requests = special_requests
        self.status = status
        
    def save(self):
        db.session.add(self)
        db.session.commit()
    @staticmethod
    def get_all():
        return Reservas.query.all()
    @staticmethod
    def get_by_id(id):
        return Reservas.query.get(id)
    def update(self,name=None,user_id=None,restaruan_id=None,reservation_date=None,num_guests=None,special_requests=None,status = None):
        if name is not None:
            self.name = name
        if user_id is not None:
            self.user_id = user_id
        if restaruan_id is not None:
            self.restaruan_id = restaruan_id
        if reservation_date is not None:
            self.reservation_date = reservation_date
        if num_guests is not None:
            self.num_guests = num_guests
        if special_requests is not None:
            self.special_requests = special_requests
        if status is not None:
            self.status = status
        db.session.commit()
            
    def delete(self):
        db.session.delete(self)
        db.session.commit()