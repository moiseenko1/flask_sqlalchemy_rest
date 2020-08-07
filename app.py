from flask import Flask, request, jsonify
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import logging

# Init logging to app.log
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# Init app
app = Flask(__name__)

# Database
app.config.from_object(Configuration)

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)
