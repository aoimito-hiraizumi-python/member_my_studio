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

from database import User
from database import Schedule
from database import Program


from werkzeug.security import generate_password_hash  # 暗号化
from werkzeug.security import check_password_hash  # パスワードに戻す

user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("/user")
def user_welcome():
    return render_template("user/user_welcome.html")


@user_bp.route("/member_signup")
def member_signup():
    return render_template("user/member_signup.html")


@user_bp.route("/member_signup", methods=["POST"])
def member_register():
    membership_number = request.form["membership_number"]
    name = request.form["name"]
    password = request.form["password"]
    generate_password_hash(password, method="sha256")
    birthday = request.form["birthday"]
    gender = request.form["gender"]
    week1 = request.form["week1"]
    week2 = request.form["week2"]
    week3 = request.form["week3"]
    time_zone1 = request.form["time_zone1"]
    time_zone2 = request.form["time_zone2"]
    User.create(
        membership_number=membership_number,
        name=name,
        password=generate_password_hash(password, method="sha256"),
        birthday=birthday,
        gender=gender,
        week1=week1,
        week2=week2,
        week3=week3,
        time_zone1=time_zone1,
        time_zone2=time_zone2,
    )
    return redirect("/user/member_login")


@user_bp.route("/member_login")
def member_login():
    return render_template("user/member_login.html")


@user_bp.route("/member_login", methods=["POST"])
def member_login_post():
    name = request.form["name"]
    password = request.form["password"]
    user = User.get(name=name)
    if check_password_hash(user.password, password):
        login_user(user)
        return redirect("/user/member_index")
    return redirect("/user/member_login")


@user_bp.route("/member_index", methods=["POST"])
# @login_required
def member_index():
    return render_template("/user/member_index.html")


@user_bp.route("/member_studio_pick")
def member_studio_pick():
    schedule = Schedule.select()
    return render_template("/user/member_studio_pick.html", schedule=schedule)


@user_bp.route("/member_class", methods=["POST"])
def member_class():
    program = request.form["program"]
    detail = Program.get(name=program)
    content = detail.content
    strength = detail.strength
    difficulty = detail.difficulty
    return render_template("/user/member_class.html", content=content, strength=strength, difficulty=difficulty)


@user_bp.route("/member_comment")
def member_comment():
    return render_template("/user/member_comment.html")


@user_bp.route("/member_reserve")
def member_reserve():
    return render_template("/user/member_reserve.html")


@user_bp.route("/member_reserved")
def member_reserved():
    return render_template("/user/member_reserved.html")


@user_bp.route("/member_walk_up")
def member_walk_up():
    return render_template("/user/member_walk_up.html")


@user_bp.route("/member_mypage")
def member_my_page():
    user = User.select()
    return render_template("/user/member_mypage.html", user=user)


@user_bp.route("/member_logout", methods=["POST"])
def member_logout():
    logout_user()
    return redirect("/user/user")


@user_bp.route("/guests")
def guests():
    return render_template("/user/guests.html")


@user_bp.route("/guests_class")
def guests_class():
    return render_template("/user/guests_class.html")
