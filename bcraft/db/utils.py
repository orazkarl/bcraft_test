from sqlalchemy import select
from sqlalchemy.orm import Session


def create_object(
        *,
        db: Session,
        data: dict,
        db_model: type
):
    obj_from_db = db_model(**data)
    db.add(obj_from_db)
    db.commit()
    return obj_from_db
