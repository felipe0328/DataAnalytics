from dal.db import db


class PurchaseAnalitics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    element_type_id = db.Column(db.Integer, db.ForeignKey(
        'element_type.id'), nullable=False)
    purchase_amount = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=db.func.now())
