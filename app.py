import os
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

from flask_login import LoginManager
from flask_login import login_required


from database import User

app = Flask(__name__)

from user import user_bp

app.register_blueprint(user_bp)

from admin import admin_bp

app.register_blueprint(admin_bp)

from ir import ir_bp

app.register_blueprint(ir_bp)

app.config["SECRET_KEY"] = os.urandom(24)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return User.get(id=int(id))


@login_manager.unauthorized_handler
def unauthorized():
    return redirect("/user/user")


# 会員・ゲスト画面


# 管理画面(クラブ側)


# IR画面


if __name__ == "__main__":
    app.run(debug=True)
