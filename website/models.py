from . import database
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(database.Model, UserMixin):
    # Creates the columns for the user
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(50), unique=True)
    password = database.Column(database.String(150))
    # Will be generated randomly with every user
    token = database.Column(database.String(30), unique=True)
    date_created = database.Column(database.DateTime(timezone=True), default=func.now())
    

class Parts(database.Model):
    # Creates the columns for the parts
    id = database.Column(database.Integer, primary_key=True)
    part_number = database.Column(database.Text, nullable=False)
    part_name = database.Column(database.Text, nullable=False)
    quantity = database.Column(database.Text, nullable=False)
    notes = database.Column(database.Text)


class PickingSlip(database.Model):
    # For picking slip
    id = database.Column(database.Integer, primary_key=True)
    part_number = database.Column(database.Text, nullable=False)
    part_name = database.Column(database.Text, nullable=False)
    quantity = database.Column(database.Text, nullable=False)
    # Date picking slip was generated
    date = database.Column(database.DateTime(timezone=True), default=func.now())
    