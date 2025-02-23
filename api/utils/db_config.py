from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
db.unique_constraint = db.UniqueConstraint