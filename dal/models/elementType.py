from dal.db import db


class ElementType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    element_name = db.Column(db.String(100), nullable=False)
