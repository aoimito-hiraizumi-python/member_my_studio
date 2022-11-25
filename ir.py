import os

from flask import Blueprint
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

from flask_login import LoginManager
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user

from database import Ir

from werkzeug.security import generate_password_hash # 暗号化
from werkzeug.security import check_password_hash    # パスワードに戻す

ir_bp = Blueprint('ir', __name__, url_prefix='/ir')

@ir_bp.route("/ir")
def ir():
    return render_template("ir/ir_welcome.html")

@ir_bp.route("ir_signup")
def ir_signup():
    return render_template("/ir/ir_signup.html")

@ir_bp.route("/ir_signup", methods=["POST"])
def ir_register():
    name = request.form["name"]
    password = request.form["password"]
    generate_password_hash(password, method="sha256")
    email = request.form["email"]
    Ir.create(
        name=name,
        password=generate_password_hash(password, method="sha256"),
        email=email
    )
    return redirect("/admin/admin_login")

@ir_bp.route("/ir_login")
def ir_login():
    return render_template("ir/ir_login.html")

@ir_bp.route("/ir_login", methods=["POST"])
def ir_login_post():
    name = request.form["name"]
    password = request.form["password"]
    ir = Ir.get(name=name)
    if check_password_hash(ir.password, password):
        login_user(ir)
        return redirect("ir/ir_index")
    return redirect("/ir/ir_login")


@ir_bp.route("/ir_index")
def ir_index():
    return render_template("ir/ir_index.html")

@ir_bp.route("/ir_pick")
def ir_pick():
    return render_template("ir/ir_pick.html")

@ir_bp.route("/ir_mypage")
def ir_mypage():
    return render_template("ir/ir_mypage.html")

@ir_bp.route("/ir_logout", methods=["POST"])
def ir_logout():
    logout_user()
    return redirect("/ir/ir")
    

@ir_bp.route("/ir_message")
def ir_message():
    return render_template("ir/ir_message.html")

@ir_bp.route("/ir_comments")
def ir_comments():
    return render_template("ir/ir_comments.html")
