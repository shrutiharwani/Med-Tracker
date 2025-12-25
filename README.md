# MedTrack

MedTrack is a Flask-based medical tracking web application that helps users manage their health data securely and efficiently.

---

## Features

- User registration and login
- Medicine tracking with dose and time
- Google Calendar reminders for medicines
- Symptom tracking with basic remedies
- Doctor appointment management
- Emergency contact storage
- Separate dashboard for each user

---

## Tech Stack

- Python
- Flask
- SQLite
- SQLAlchemy
- Flask-Login
- Flask-WTF
- HTML, CSS, Jinja2
- Google Calendar API
- Google Maps

---

## Project Structure

```
medtrack/
│
├── app.py
├── extensions.py
├── models.py
├── forms.py
├── routes_main.py
├── reset_db.py
├── requirements.txt
│
├── static/
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   ├── medicines.html
│   ├── symptoms.html
│   ├── appointments.html
│   └── contacts.html
│
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/your-username/medtrack.git
cd medtrack
```

Create virtual environment:

```
python -m venv venv
```

Activate it:

Windows:
```
venv\Scripts\activate
```

Mac/Linux:
```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## Google Calendar Setup

1. Create a Google Cloud project
2. Enable Google Calendar API
3. Download `credentials.json`
4. Place it in the project root
5. Login once to grant permission

---

