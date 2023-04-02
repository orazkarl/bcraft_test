from datetime import date

from sqlalchemy import Column, Date, Integer, Float
from sqlalchemy.orm import column_property

from bcraft.db.base_model import BaseModel


class Statistics(BaseModel):
    date: date = Column(Date)
    views: int = Column(Integer)
    clicks: int = Column(Integer)
    cost: float = Column(Float)

    @property
    def cpc(self):
        if self.cost and self.clicks:
            return self.cost / self.clicks
        return None

    @property
    def cpm(self):
        if self.cost and self.views:
            return self.cost / self.views * 1000
        return None

