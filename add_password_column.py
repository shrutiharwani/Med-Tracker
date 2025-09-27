from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

# Connect directly to the SQLite database
conn = sqlite3.connect('app.db')
cursor = conn.cursor()

# Add password column if it doesn't exist
try:
    cursor.execute("ALTER TABLE user ADD COLUMN password TEXT;")
    print("Password column added successfully!")
except sqlite3.OperationalError as e:
    print("Error:", e)

conn.commit()
conn.close()
