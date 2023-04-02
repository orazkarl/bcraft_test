from datetime import date
from typing import Optional

from pydantic import BaseModel, root_validator, Field


class StatisticsCreateSchema(BaseModel):
    date: date
    views: Optional[int] = Field(ge=0)
    clicks: Optional[int] = Field(ge=0)
    cost: Optional[float] = Field(ge=0)


class StatisticsResponseModel(BaseModel):
    date: date
    views: Optional[int]
    clicks: Optional[int]
    cost: Optional[float]
    cpc: Optional[float]
    cpm: Optional[float]

    class Config:
        orm_mode = True
