from flask import Blueprint, render_template, request, flash, url_for,redirect
from helpers import login_required

from db import get_companies, get_company, add_company, update_company

settings = Blueprint('settings', __name__,url_prefix="/settings")

retVal = list()

""" COMPANY ACTIONS """
@settings.route("/company/list")
@login_required
def company_list():
    if request.method == "GET":
        rows, cnt = get_companies()
        return render_template("company_list.html", rows=rows, count=cnt)
    # else:
    #     id = request.form.get("id")
    #     data = get_company(id)
    #     retVal = list(data)
    #     return company_update()
        #return render_template("company_update.html", name=retVal[1], erp=retVal[2],address=retVal[3],web=retVal[4])
        #return redirect(url_for("settings.company_update", name=retVal[1], erp=retVal[2],address=retVal[3],web=retVal[4]))

@settings.route("/company/new" , methods=["GET","POST"])
@login_required
def company_new():
    if request.method == "GET":
        return render_template("company_new.html")
    else:
        company_name = request.form.get("company_name")
        erp_code = request.form.get("erp_code")
        address = request.form.get("address")
        web_address = request.form.get("web_address")
        if not company_name or not erp_code or not address or not web_address:
            flash("Missing informations!")
            return redirect(url_for("settings.company_new"))
        else:
            retVal = add_company(company_name, erp_code, address, web_address)
            flash(retVal)
            return redirect(url_for("settings.company_list"))

@settings.route("/company/update", methods=["POST"])
@login_required
def company_update():
    id = request.form.get("id")
    company_name = request.form.get("company_name")
    erp_code = request.form.get("erp_code")
    address = request.form.get("address")
    web_address = request.form.get("web_address")
    print(company_name, erp_code, address, web_address)
    retVal = update_company(id,company_name, erp_code, address, web_address)
    flash(retVal)
    return redirect(url_for("settings.company_list"))




""" DEPARTMENT ACTIONS """
@settings.route("/department")
@login_required
def department():
    return render_template("department.html")