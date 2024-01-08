from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/home')

def home():
    return render_template("home.html")


# @views.route('/sign_up')

# def home():
#     return render_template("sign_up.html")


# @views.route('/login')

# def home():
#     return render_template("login.html")