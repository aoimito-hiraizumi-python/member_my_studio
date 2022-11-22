from flask import Flask
from flask import render_template
from flask import redirect


app = Flask(__name__)

@app.route("/")
def user_welcome():
    return render_template("user_welcome.html")

@app.route("/member_login", methods=["POST"])
def member_login():
    return render_template("member_login.html")

@app.route("/member_signup", methods=["POST"])
def member_signup():
    return render_template("member_signup.html")

@app.route("/member_index", methods=["POST"])
def member_index():
    return render_template("member_index.html")

@app.route("/member_studio_pick", methods=["POST"])
def member_studio_pick():
    return render_template("member_studio_pick.html")

@app.route("/member_class", methods=["POST"])
def member_class():
    return render_template("member_class.html")

@app.route("/member_comment", methods=["POST"])
def member_comment():
    return render_template("member_comment.html")

@app.route("/member_reserve", methods=["POST"])
def member_reserve():
    return render_template("member_reserve.html")

@app.route("/reserved", methods=["POST"])
def reserved():
    return render_template("reserved.html")

@app.route("/member_my_page", methods=["POST"])
def member_my_page():
    return render_template("member_my_page.html")

@app.route("/logout", methods=["POST"])
def logout():
    return redirect("/")

@app.route("/guests", methods=["POST"])
def guests():
    return render_template("guests.html")

@app.route("/guests_class", methods=["POST"])
def guests_class():
    return render_template("guests_class.html")




if __name__ == "__main__":
    app.run(debug=True)
