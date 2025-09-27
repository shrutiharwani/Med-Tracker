# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, TimeField, TextAreaField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=3, max=120)])
    email = StringField('Email', validators=[InputRequired(), Email(), Length(max=200)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(), Length(max=200)])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class MedicineForm(FlaskForm):
    name = StringField('Medicine Name', validators=[InputRequired(), Length(max=150)])
    dose = StringField('Dose (e.g. 1 tablet)', validators=[InputRequired(), Length(max=80)])
    time = TimeField('Time', validators=[InputRequired()])
    submit = SubmitField('Add Medicine')

class SymptomForm(FlaskForm):
    symptom_text = StringField('Describe symptom', validators=[InputRequired(), Length(max=300)])
    submit = SubmitField('Add Symptom')

class AppointmentForm(FlaskForm):
    doctor = StringField('Doctor / Clinic', validators=[InputRequired(), Length(max=150)])
    specialty = StringField('Specialty', validators=[Length(max=120)])
    date = DateField('Date', validators=[InputRequired()])
    time = TimeField('Time')
    address = StringField('Address / Clinic', validators=[Length(max=300)])
    notes = TextAreaField('Notes', validators=[Length(max=800)])
    submit = SubmitField('Book Appointment')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(max=150)])
    phone = StringField('Phone', validators=[InputRequired(), Length(max=50)])
    relation = StringField('Relation', validators=[Length(max=100)])
    submit = SubmitField('Add Contact')
