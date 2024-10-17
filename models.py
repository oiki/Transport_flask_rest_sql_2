from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Transport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    transport_type = db.Column(db.String(50), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')
