from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_restful import Api, Resource


database = SQLAlchemy()
DB_NAME = "picker.db"

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = "123456789"
    
    # Settting up the database for forms
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    database.init_app(app)    
    
    # Relative imports for all the views
    from .views import views
    
    # Blueprint for each of the views, the prefix is set to none, can set to other if need be
    app.register_blueprint(views)
    
    # Import the database that was created for the users from models.py
    from .models import User, Parts, PickingSlip
    
    '''
    with app.app_context():
        database.create_all()
        '''
    
    # Used so that user can access some pages that others cant
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app


def create_database(app):
    # Creates the database if it does not eist
    if not path.exists("website/" + DB_NAME):
        database.create_all(app=app)
        