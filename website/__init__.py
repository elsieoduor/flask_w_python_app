from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
  app = Flask(__name__) #Reps name of file. This is for initialization
  app.config['SECRET_KEY']= 'yukiosrandomshit'
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

  db.init_app(app)

  from .views import views
  from .auth import auth

  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')
  
  return app