""" this module initializes the database with some mock data """
import pandas as pd
from werkzeug.security import generate_password_hash, check_password_hash

from app import app
from database import db
from models import Doctor


# test 1
new_doctor = Doctor(
    email = "new_doc@mail.com",
    first = "John",
    last = "Doe",
    specialty = "Cardiology",
    hospital = "Idanre Teaching Hospital",
    city = "Ilua",
    rank = "Consultant",
    phone = "232-222-111",
    password = generate_password_hash('John_password')
)
with app.app_context():
    new_doctor.register_doctor()

# # load the csv of the mock data
# df = pd.read_csv('doctors.csv')
# # hash the passwords in the mock data
# df.password = df.password.apply(lambda x:generate_password_hash(x))
# print(df.head())


# with app.app_context():
#     df = pd.read_csv('doctors.csv')
#     for index, row in df.iterrows():
#         new_doctor = Doctor(
#             email = row.email,
#             first = row.first_name,
#             last = row.last_name,
#             specialty = row.specialty,
#             hospital = row.hospital,
#             city = row.city,
#             rank = row.ranking,
#             phone = row.phone,
#             password = generate_password_hash(row.password)
#         )
#         db.session.add(new_doctor)
#     db.session.commit()
#     # doctor = Doctor.query.limit(1).all()[0]
#     # unhashed = check_password_hash(doctor.password, 'John_password')
#     print(Doctor.query.limit(5).all())
