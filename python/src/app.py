from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create Flask Application
application = Flask(__name__)

# Set Config Class
application.config.from_object(Config)

# Set DB
db = SQLAlchemy(application)
