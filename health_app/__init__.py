from flask import Flask
from os import path
from flask_login import LoginManager
import boto3


db = boto3.resource('dynamodb') #connect to dynamodb
table = db.Table('users') # type: ignore #connect to table


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "hjshjhdjah kjshkjdhjs"
    #app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    #db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User
    #create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(email):
        return table.get_item(Key={'email': email})

    return app

"""
def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created Database!")
"""
