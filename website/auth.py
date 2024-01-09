from flask import Blueprint, render_template, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    data = request.form
   
    return render_template("login.html", boolean=True)


@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        pass1 = request.form.get("pass1")
        pass2 = request.form.get("pass2")

        if len(email)<4:
            flash("Email must be greater than 4 character", category="error")

        elif len(firstName)<2:
            flash("First name must be greater that 2 characters", category="error")
        
        elif pass1 != pass2:
            flash("Password dont\'t match", category="error")

        elif len(pass1)<7:
            flash("Password must be equal or greater than 8 characters", category="error")

        else:
            newUser = User(email=email, firstName=firstName, password=generate_password_hash(pass1, method="sha256"))
            flash("Account Created!!", category="success")


        # print(email, firstName, pass1, pass2)
        

    return render_template("sign_up.html")


@auth.route("/home")

def home():
    
    return render_template("home.html")