from dal.db import db


class PurchaseAnalitics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    
