from main import db


class usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    
    __tablename__ = 'sexo'