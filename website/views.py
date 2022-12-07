from distutils.log import error
from flask import Blueprint, flash, render_template, redirect, url_for, request, session
from . import database
import re
from .models import Parts, PickingSlip
from flask_login import login_required
from werkzeug.security import generate_password_hash, check_password_hash

views = Blueprint("views", __name__, url_prefix="/")

@views.route("/", methods=["GET", "POST"])
@views.route("/home", methods=["GET", "POST"])
@login_required
def home():
    
    return render_template("home.html")
