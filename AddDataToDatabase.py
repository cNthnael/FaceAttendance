import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pythfacerec-default-rtdb.firebaseio.com/'
})

ref = db.reference('Attendances')

data = {
    "2301901444":
        {
            "name": "Galih PRAMUDYA",
            "major": "Informatika",
            "starting_year": 2019,
            "total_attendance": 6,
            "standing": "Good",
            "year": 4,
            "last_attendance_time": "2023-07-26 18:01:33"
        },
    "2440105495":
        {
            "name": "Dzakwan AMIRUL",
            "major": "Informatika",
            "starting_year": 2020,
            "total_attendance": 4,
            "standing": "Average",
            "year": 3,
            "last_attendance_time": "2023-07-26 18:08:33"
        },
    "2440106365":
        {
            "name": "Carlo NATHANAEL",
            "major": "Informatika",
            "starting_year": 2020,
            "total_attendance": 6,
            "standing": "Good",
            "year": 3,
            "last_attendance_time": "2023-07-26 18:11:33"
        },
    "2440108950":
        {
            "name": "Marco SAJID",
            "major": "Informatika",
            "starting_year": 2020,
            "total_attendance": 6,
            "standing": "Good",
            "year": 3,
            "last_attendance_time": "2023-07-26 18:14:33"
        },
}

for key, value in data.items():
    ref.child(key).set(value)
