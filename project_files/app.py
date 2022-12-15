from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
#from flask_sqlalchemy import SQLAlchemy

# Import the necessary classes for connecting to a Hyperledger Fabric network
#from hyperledger.fabric import FabricClient

# Create the Flask app and set up the LoginManager
app = Flask(__name__)
#db = SQLAlchemy(app)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db" # Set the database URI
app.config["SECRET_KEY"] = "secret#0770"
login_manager = LoginManager()
login_manager.init_app(app)

# Set up the Fabric client
#fabric = FabricClient()

# Define the user class for doctors and patients
"""class User(db.Model, UserMixin):
    id= db.Column(db. Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password= db.Column(db.String(80), nullable=False)
"""
class User:
    def __init__(self, username, password, is_doctor):
        self.username = username
        self.password = password
        self.is_doctor = is_doctor

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username


# Define the route for the home page
@app.route("/")
def home():
    if current_user.is_authenticated:
        # If the user is logged in, show their dashboard
        if current_user.is_doctor:
            # Show the doctor's dashboard
            return render_template("doctor_dashboard.html")
        else:
            # Show the patient's dashboard
            return render_template("patient_dashboard.html")
    else:
        # If the user is not logged in, show the login page
        return render_template("login.html")


# Define the route for logging in
@app.route("/login", methods=["POST"])
def login():
    # Get the username and password from the request
    username = request.form["username"]
    password = request.form["password"]

    # Look up the user in the Fabric network
    user_data = fabric.query("getUser", [username])

    # If the user exists, check the password and log them in
    if user_data:
        if user_data["password"] == password:
            user = User(username, password, user_data["is_doctor"])
            login_user(user)
            return redirect(url_for("home"))
        else:
            # If the password is incorrect, show an error message
            return render_template("login.html", error="Incorrect password")
    else:
        # If the user does not exist, show an error message
        return render_template("login.html", error="User does not exist")


# Define the route for logging out
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


# Define the route for the doctor's patient list page
@app.route("/patients")
@login_required
def patients():
    # Check if the user is a doctor and is logged in
    if current_user.is_authenticated and current_user.is_doctor:
        # Get the list of patients from the Fabric network
        patient_list = fabric.query("getPatients")

        return render_template("patients.html", patients=patient_list)

if __name__ == "__main__":
    app.run(debug=True)
