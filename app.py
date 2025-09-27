from flask import Flask, render_template
from extensions import db, login_manager
from datetime import datetime
from flask_migrate import Migrate

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'replace_this_with_a_real_secret'  # Change to a strong secret in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medtrack.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
login_manager.init_app(app)
migrate = Migrate(app, db)


# Import models
from models import User

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Import and register blueprint
from routes_main import main_blueprint
app.register_blueprint(main_blueprint, url_prefix='')

# Context processor to inject current year into all templates
@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}


@app.route('/')
def dashboard():
    return render_template("dashboard.html")


# Create database tables and run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Remove debug=True in production
