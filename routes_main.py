from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models import User, Medication

main_blueprint = Blueprint('main', __name__)

# -------------------------------
# Home / Index Page
# -------------------------------
@main_blueprint.route('/')
@login_required
def index():
    medications = Medication.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', medications=medications)

# -------------------------------
# User Registration
# -------------------------------
@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash("All fields are required!", "error")
            return redirect(url_for('main.register'))

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists!", "error")
            return redirect(url_for('main.register'))

        new_user = User(
            username=username,
            password=generate_password_hash(password)
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Account created! Please log in.", "success")
        return redirect(url_for('main.login'))

    return render_template('register.html')

# -------------------------------
# User Login
# -------------------------------
@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            flash("Invalid username or password", "error")
            return redirect(url_for('main.login'))

        login_user(user)
        flash(f"Welcome, {username}!", "success")
        return redirect(url_for('main.index'))

    return render_template('login.html')

# -------------------------------
# User Logout
# -------------------------------
@main_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully!", "success")
    return redirect(url_for('main.login'))

# -------------------------------
# Add Medication
# -------------------------------
@main_blueprint.route('/add_medication', methods=['POST'])
@login_required
def add_medication():
    med_name = request.form.get('med_name')
    dosage = request.form.get('dosage')
    frequency = request.form.get('frequency')

    if not med_name or not dosage or not frequency:
        flash("All fields are required!", "error")
        return redirect(url_for('main.index'))

    new_med = Medication(
        name=med_name,
        dosage=dosage,
        frequency=frequency,
        user_id=current_user.id
    )
    db.session.add(new_med)
    db.session.commit()
    flash(f"{med_name} added successfully!", "success")
    return redirect(url_for('main.index'))

# -------------------------------
# Delete Medication
# -------------------------------
@main_blueprint.route('/delete_medicine/<int:med_id>', methods=['POST'])
@login_required
def delete_medicine_route(med_id):
    med = Medication.query.get_or_404(med_id)
    if med.user_id != current_user.id:
        flash("You cannot delete this medication!", "error")
        return redirect(url_for('main.index'))

    db.session.delete(med)
    db.session.commit()
    flash(f"{med.name} deleted successfully!", "success")
    return redirect(url_for('main.index'))

# -------------------------------
# Placeholder Pages
# -------------------------------
@main_blueprint.route('/symptoms')
@login_required
def symptoms_page():
    return render_template('symptoms.html')

@main_blueprint.route('/appointments')
@login_required
def appointments_page():
    return render_template('appointments.html')

@main_blueprint.route('/contacts')
@login_required
def contacts_page():
    return render_template('contacts.html')
