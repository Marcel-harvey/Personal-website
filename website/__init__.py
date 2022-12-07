from flask import Flask, render_template, session
from os import path


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = "123456789"
    
    # Relative imports for all the views
    from .views import views
    
    # Blueprint for each of the views, the prefix is set to none, can set to other if need be
    app.register_blueprint(views)
    
    # Import the database that was created for the users from models.py
    from .models import User, Parts, PickingSlip
    
    return app
        