from . import db
from flask_login import UserMixin
from datetime import date

class User(db.Model, UserMixin):
    __tablename__ = 'users'  # Match existing table

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(128), nullable=False)  # add hashed password
    date_added = db.Column(db.Date, default=date.today)

    def get_id(self):
        return str(self.user_id)