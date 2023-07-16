from dal.db import db
from dal.models.elementType import ElementType


def find_or_create_element_type_by_name(elementTypeName: str) -> int:
    foundElement = ElementType.query.filter_by(
        element_name=elementTypeName).first()

    if foundElement == None:
        newElement = ElementType(element_name=elementTypeName)
        db.session.add(newElement)
        db.session.commit()
        return newElement.id

    return foundElement.id
