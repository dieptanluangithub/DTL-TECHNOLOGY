from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager
import cloudinary

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:0898654463@localhost/utesaleapp?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key = "tanluandiep"
app.config["PAGE_SIZE"] =8
app.config["CLOUDINARY_INFO"] = {
    "cloud_name": "tanluandiep",
    "api_key": "962924331539285",
    "api_secret": "PljWZPgZdr8HtJ66FKGENm-5XoY"
}


db = SQLAlchemy(app=app)
my_login = LoginManager(app=app)
CART_KEY = "cart"

cloudinary.config(cloud_name=app.config["CLOUDINARY_INFO"]['cloud_name'],
                                      api_key=app.config["CLOUDINARY_INFO"]['api_key'],
                                      api_secret=app.config["CLOUDINARY_INFO"]['api_secret'])