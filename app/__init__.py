from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object("config.Config")
db = SQLAlchemy(app)

from . import modules, forms, views

db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
