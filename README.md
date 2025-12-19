# MedTrack — Personal Medical Tracking Web App

MedTrack is a Flask-based medical tracking web application that helps users manage their health information in one place.  
Users can track medicines, symptoms, doctor appointments, and emergency contacts securely.

---

## Features

### User Authentication
- Secure login and registration
- Separate dashboard for each user
- Password hashing using Werkzeug

### Medicine Tracking
- Add medicine name, dose, and time
- Automatic reminders using Google Calendar
- View and remove medicines

### Symptom Tracking
- Add daily symptoms
- Displays basic remedies for common symptoms
- Helps monitor health patterns

### Doctor Appointments
- Schedule doctor appointments
- Store doctor name, specialty, date, and notes
- Google Maps integration for location assistance

### Emergency Contacts
- Add emergency contact name and phone number
- Quick access during emergencies
- Remove contacts when needed

---

## Tech Stack

| Layer | Technology |
|-----|-----------|
| Backend | Flask (Python) |
| Database | SQLite |
| ORM | SQLAlchemy |
| Authentication | Flask-Login |
| Forms | Flask-WTF |
| APIs | Google Calendar, Google Maps |
| Frontend | HTML, CSS, Jinja2 |

---

## Project Structure

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
│ └── style.css
│
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── dashboard.html
│ ├── login.html
│ ├── register.html
│ ├── medicines.html
│ ├── symptoms.html
│ ├── appointments.html
│ └── contacts.html
│
└── README.md

yaml
Copy code

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/medtrack.git
cd medtrack
2. Create Virtual Environment
bash
Copy code
python -m venv venv
Activate it:

Windows

bash
Copy code
venv\Scripts\activate
Mac/Linux

bash
Copy code
source venv/bin/activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Run the Application
bash
Copy code
python app.py
Open your browser and visit:

cpp
Copy code
http://127.0.0.1:5000/
