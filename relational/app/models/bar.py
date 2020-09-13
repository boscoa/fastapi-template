from typing import Any

from pydantic import BaseModel, Field


class BarBase(BaseModel):
    foo: str
    bar: str


class BarContract(BarBase):
    pass


class BarMongo(BarContract):
    mongo_id: Any = Field(None, alias='_id')


class Bar(BarContract):
    bar_id: str = None
