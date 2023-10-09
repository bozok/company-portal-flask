from flask import Blueprint, render_template

from helpers import login_required

site = Blueprint('site', __name__)

@site.route("/")
@login_required
def index():
    return render_template("index.html")


# @site.route("/company")
# @login_required
# def company():
#     return render_template("company.html")