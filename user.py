import os

from flask import Blueprint
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

from flask_login import LoginManager
from flask_login import login_required

from database import User
user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route("/user")
def user_welcome():
    return render_template("user/user_welcome.html")

@user_bp.route("/member_login")
def member_login():
    return render_template("user/member_login.html")

@user_bp.route("/member_signup")
def member_signup():
    return render_template("user/member_signup.html")

# @user_bp.route("/member_signup", methods=["POST"])
# def member_register():
#     membership_number = request.form["membership_number"]
#     name = request.form["name"]
#     password = request.form["password"]
#     birthday = request.form["birthday"]
#     gender = request.form["gender"]
#     week = request.form["week"]
#     time_zone = request.form["time_zone"]
#     User.create(
#         membership_number=membership_number,
#         name=name,
#         password=password,
#         birthday=birthday,
#         gender=gender,
#         week=week,
#         time_zone=time_zone
#     )
#     return redirect("user//user_login")

@user_bp.route("member_index")
# @login_required
def member_index():
    return render_template("user/member_index.html")

@user_bp.route("/member_studio_pick")
def member_studio_pick():
    return render_template("user/member_studio_pick.html")

@user_bp.route("/member_class")
def member_class():
    return render_template("user/member_class.html")

@user_bp.route("/member_comment")
def member_comment():
    return render_template("user/member_comment.html")

@user_bp.route("/member_reserve")
def member_reserve():
    return render_template("user/member_reserve.html")

@user_bp.route("/member_reserved")
def member_reserved():
    return render_template("user/member_reserved.html")

@user_bp.route("/member_walk_up")
def member_walk_up():
    return render_template("user/member_walk_up.html")

@user_bp.route("/member_mypage")
def member_my_page():
    return render_template("user/member_mypage.html")

@user_bp.route("/member_logout")
def member_logout():
    return redirect("user/user")

@user_bp.route("/guests")
def guests():
    return render_template("user/guests.html")

@user_bp.route("/guests_class")
def guests_class():
    return render_template("user/guests_class.html")
