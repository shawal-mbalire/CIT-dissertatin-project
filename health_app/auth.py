from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from . import db,table
import hashlib

auth = Blueprint("auth", __name__)

# login route
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        encoded_password = password.encode()

        # query database for user
        response = table.get_item(
            Key={
                'username': username,
                'password': password
            }
        )
        user = response['Item']

        # check if user exists
        if user:
            #check if password is correct
            if (hashlib.sha256(encoded_password).hexdigest()==user[password]):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                if (user['role']=='doctor'):return redirect(url_for('views.doctor_dashboard'))
                if (user['role']=='patient'):return redirect(url_for('views.patient_dashboard'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

# logout route
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

# sign up route
@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # Get the form data from the request object
        username = request.form["username"]
        age = request.form["age"]
        email = request.form["email"]
        gender = request.form["gender"]
        insurance = request.form["insurance"]
        surname = request.form["surname"]
        other_name = request.form["otherName"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        phone_number = request.form["phoneNumber"]
        role = request.form["role"]

        # hash password
        encoded_password = password1.encode('utf-8')
        password = hashlib.sha256(encoded_password).hexdigest()

        # query database for user
        response = table.get_item(
            Key={
                'username': username,
                'password': password
            }
        )
        try:user = response['Item']
        except:user = None

        if user:#check if user exists
            flash("Email already exists.", category="error")
        elif len(email) < 4:#check if email is valid
            flash("Email must be greater than 3 characters.", category="error")
        elif len(surname) < 2:#check if first name is valid
            flash("First name must be greater than 1 character.", category="error")
        elif password1 != password2:#check if passwords match
            flash("Passwords don't match.", category="error")
        elif len(password1) < 7:#check if password is valid
            flash("Password must be at least 7 characters.", category="error")
        elif not username:
            flash("Please enter a username.")
        elif not age:
            flash("Please enter your age.")
        elif not email:
            flash("Please enter your email.")
        elif not gender:
            flash("Please select your gender.")
        elif not insurance:
            flash("Please enter your insurance provider.")
        elif not surname:
            flash("Please enter your surname.")
        elif not other_name:
            flash("Please enter your other name.")
        elif not phone_number:
            flash("Please enter your phone number.")
        elif not role:
            flash("Please select your role.")
        else:#create new user
            table.put_item(
                Item={
                "username": username,
                "password": password1,
                "age": age,
                "email": email,
                "gender": gender,
                "insurance": insurance,
                "surname": surname,
                "other_name": other_name,
                "phone_number": phone_number,
                "role": role,
                "records": {}
                }
            )
        login_user(username, remember=True)
        print("Account created!\n")
        flash("Account created!", category="success")
        if (role=='doctor'):return redirect(url_for('views.doctor_dashboard'))
        if (role=='patient'):return redirect(url_for('views.patient_dashboard'))
    return render_template("sign_up.html", user=current_user)




