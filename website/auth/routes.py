from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash
from db import get_time


auth = Blueprint('auth', __name__, url_prefix="/auth")

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if not request.form.get("username") or not request.form.get("password"):
            flash('Missing login credentials')
            redirect(url_for("auth.login"))
        else:
            session["user_id"] = 1
            return redirect("/")
        #get_time()
    else:
        return render_template("login.html")
    

@auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("site.index"))
    
