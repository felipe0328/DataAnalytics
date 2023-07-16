from dal.db import db
from dal.models.purchaseAnalitics import PurchaseAnalitics
from dal.analitics.elementType import find_or_create_element_type_by_name


def insert_new_analitics_entry(purchasesByType:dict[str, str]):
    for key in purchasesByType:
        elementTypeId = find_or_create_element_type_by_name(key)
        newEntry =PurchaseAnalitics(element_type_id=elementTypeId, purchase_amount=purchasesByType[key])
        db.session.add(newEntry)
        db.session.commit()