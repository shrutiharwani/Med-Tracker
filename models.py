from extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# -------------------------------
# User Model
# -------------------------------
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    medications = db.relationship('Medication', backref='user', lazy=True)
    symptoms = db.relationship('Symptom', backref='user', lazy=True)
    appointments = db.relationship('Appointment', backref='user', lazy=True)
    contacts = db.relationship('Contact', backref='user', lazy=True)

    def set_password(self, password_plain):
        self.password = generate_password_hash(password_plain)

    def check_password(self, password_plain):
        return check_password_hash(self.password, password_plain)

# -------------------------------
# Medication Model
# -------------------------------
class Medication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    dosage = db.Column(db.String(80), nullable=False)
    frequency = db.Column(db.String(50), nullable=False)
    google_event_id = db.Column(db.String(300), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# -------------------------------
# Symptom Model
# -------------------------------
class Symptom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symptom_text = db.Column(db.String(300), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# -------------------------------
# Appointment Model
# -------------------------------
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor = db.Column(db.String(150), nullable=False)
    specialty = db.Column(db.String(120), nullable=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=True)
    address = db.Column(db.String(300), nullable=True)
    notes = db.Column(db.String(800), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# -------------------------------
# Contact Model
# -------------------------------
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    relation = db.Column(db.String(100), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
