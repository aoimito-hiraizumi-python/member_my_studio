import os

from flask import Blueprint
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

from flask_login import LoginManager
from flask_login import login_required

# from database import Admin
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route("/admin")
def admin():
    return render_template("admin/admin_welcome.html")

@admin_bp.route("/admin_login")
def admin_login():
    return render_template("admin/admin_login.html")

@admin_bp.route("/admin_signup")
def admin_signup():
    return render_template("admin/admin_signup.html")

@admin_bp.route("/admin_index")
def admin_index():
    return render_template("admin/admin_index.html")

@admin_bp.route("/admin_schedule")
def admin_schedule():
    return render_template("admin/admin_schedule.html")

@admin_bp.route("/admin_program")
def admin_program():
    return render_template("admin/admin_program.html")
    
@admin_bp.route("/admin_ir")
def admin_ir():
    return render_template("admin/admin_ir.html")

@admin_bp.route("/admin_data")
def admin_data():
    return render_template("admin/admin_data.html")
    
@admin_bp.route("/admin_mypage")
def admin_mypage():
    return render_template("admin/admin_mypage.html")

@admin_bp.route("/admin_logout")
def admin_logout():
    return redirect("admin//admin")

@admin_bp.route("/admin_reserved")
def admin_reserved():
    return render_template("admin/admin_reserved.html")

@admin_bp.route("/admin_comments")
def admin_comments():
    return render_template("admin/admin_comments.html")

@admin_bp.route("/admin_favorites")
def admin_favorites():
    return render_template("admin/admin_favorites.html")
