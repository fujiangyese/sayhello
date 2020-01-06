from flask import Flask
from flask_sqlalchemy import SQLAlchemy

print(__name__)

app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)

import views, errors, commands
