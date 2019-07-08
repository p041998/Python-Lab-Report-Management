
from flask import Flask

from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SECRET_KEY'] = '7b334778c72cf8f2c30f27c6358f589fb2d23419'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)



from flaskdemo import routes