from flask import Blueprint,flash, render_template, redirect, url_for, request, session
import re


views = Blueprint("views", __name__, url_prefix="/")

@views.route("/", methods=["GET", "POST"])
@views.route("/home", methods=["GET", "POST"])
def home():
    
    return render_template("home.html")
