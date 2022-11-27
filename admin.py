import os

from flask import Blueprint
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

from flask_login_multi import login_required
from flask_login_multi import login_user
from flask_login_multi import logout_user

from database import Admin
from database import Ir_register
from database import Program
from database import Schedule

from werkzeug.security import generate_password_hash  # 暗号化
from werkzeug.security import check_password_hash  # パスワードに戻す

# from database import Admin
admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/admin")
def admin():
    return render_template("admin/admin_welcome.html")


@admin_bp.route("/admin_signup")
def admin_signup():
    return render_template("admin/admin_signup.html")


@admin_bp.route("/admin_signup", methods=["POST"])
def admin_register():
    name = request.form["name"]
    password = request.form["password"]
    generate_password_hash(password, method="sha256")
    email = request.form["email"]
    Admin.create(
        name=name,
        password=generate_password_hash(password, method="sha256"),
        email=email,
    )
    return redirect("/admin/admin_login")


@admin_bp.route("/admin_login")
def admin_login():
    return render_template("admin/admin_login.html")


@admin_bp.route("/admin_login", methods=["POST"])
def admin_login_post():
    name = request.form["name"]
    password = request.form["password"]
    admin = Admin.get(name=name)
    if check_password_hash(admin.password, password):
        login_user(admin)
        return redirect("admin/admin_index")
    return redirect("/admin/admin_login")


@admin_bp.route("/admin_index", methods=["GET", "POST"])
@login_required
def admin_index():
    return render_template("admin/admin_index.html")


@admin_bp.route("/admin_program")
def admin_program():
    return render_template("admin/admin_program.html")


@admin_bp.route("/admin_program", methods=["POST"])
def admin_program_register():
    name = request.form["name"]
    content = request.form["content"]
    strength = request.form["strength"]
    difficulty = request.form["difficulty"]
    minutes = request.form["minutes"]
    capacity = request.form["capacity"]
    Program.create(
        name=name,
        content=content,
        strength=strength,
        difficulty=difficulty,
        minutes=minutes,
        capacity=capacity,
    )
    return redirect("/admin/admin_program")


@admin_bp.route("/admin_schedule")
def admin_schedule():
    programs = Program.select()
    irs = Ir_register.select()
    return render_template("admin/admin_schedule.html", programs=programs, irs=irs)


@admin_bp.route("/admin_schedule", methods=["POST"])
def admin_schedule_register():
    # year = request.form["year"]
    # month = request.form["month"]
    week = request.form["week"]
    time = request.form["time"]
    program = request.form["program"]
    ir = request.form["ir"]
    Schedule.create(
        # year=year,
        # month=month,
        week=week,
        time=time,
        program=program,
        ir=ir,
    )
    return redirect("/admin/admin_schedule")


@admin_bp.route("/admin_class")
def admin_class():
    return render_template("admin/admin_class.html")


@admin_bp.route("/admin_ir")
def admin_ir():
    programs = Program.select()
    return render_template("admin/admin_ir.html", programs=programs)


@admin_bp.route("/admin_ir", methods=["POST"])
def admin_ir_register():
    name = request.form["name"]
    program1 = request.form["program1"]
    fee1 = request.form["fee1"]
    program2 = request.form["program2"]
    fee2 = request.form["fee2"]
    program3 = request.form["program3"]
    fee3 = request.form["fee3"]
    email = request.form["email"]
    Ir_register.create(
        name=name,
        program1=program1,
        fee1=fee1,
        program2=program2,
        fee2=fee2,
        program3=program3,
        fee3=fee3,
        email=email,
    )
    return redirect("/admin/admin_ir")


@admin_bp.route("/admin_data")
def admin_data():
    return render_template("admin/admin_data.html")


@admin_bp.route("/admin_mypage")
def admin_mypage():
    return render_template("admin/admin_mypage.html")


@admin_bp.route("/admin_logout", methods=["POST"])
def admin_logout():
    logout_user()
    return redirect("/admin/admin")


@admin_bp.route("/admin_member")
def admin_member():
    return render_template("admin/admin_member.html")


@admin_bp.route("/admin_reserved")
def admin_reserved():
    return render_template("admin/admin_reserved.html")


@admin_bp.route("/admin_comments")
def admin_comments():
    return render_template("admin/admin_comments.html")


@admin_bp.route("/admin_favorites")
def admin_favorites():
    return render_template("admin/admin_favorites.html")
