from datetime import date
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import JSONResponse

from bcraft.api.schemas.statistics import StatisticsCreateSchema, StatisticsResponseModel
from bcraft.db import deps
from bcraft.db.utils import create_object
from bcraft.models import Statistics

router = APIRouter()


@router.post('/create')
def create(
        *,
        db: Session = Depends(deps.get_db),
        request_data: StatisticsCreateSchema
) -> JSONResponse:
    create_object(db=db, data=request_data.dict(), db_model=Statistics)
    return JSONResponse(content={}, status_code=status.HTTP_201_CREATED)


@router.post('/show', response_model=List[StatisticsResponseModel])
def show_statistics(
        *,
        db: Session = Depends(deps.get_db),
        from_date: date = date.today(),
        to_date: date = date.today()
) -> List[Statistics]:
    query = db.query(
        Statistics,
    ).filter(
        Statistics.date.between(from_date, to_date)
    ).order_by(
        Statistics.date
    )
    statistics_objects = db.execute(query)
    return statistics_objects.scalars().all()


@router.delete("/reset", status_code=status.HTTP_200_OK)
def reset_stats(
        *,
        db: Session = Depends(deps.get_db),
) -> JSONResponse:
    db.query(
        Statistics,
    ).delete()
    db.commit()
    return JSONResponse(
        content={"message": "Statistics reset successfully"},
        status_code=status.HTTP_200_OK
    )
