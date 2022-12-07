from . import database


class User(database.Model):
    # Creates the columns for the user
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(50), unique=True)
    password = database.Column(database.String(150))
    # Will be generated randomly with every user
    token = database.Column(database.String(30), unique=True)
    date_created = database.Column(database.DateTime(timezone=True))
    