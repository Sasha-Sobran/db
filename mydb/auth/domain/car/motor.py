from __future__ import annotations

from typing import Dict, Any

from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class Motor(IDto, db.Model):
    __tablename__ = "motor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    power = Column(Float, nullable=False)

    cars = relationship("Car", back_populates="motor")

    def __repr__(self):
        return f"Motor(id={self.id}, power={self.power})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Motor:
        obj = Motor(
            id=dto_dict.get("id"),
            power=dto_dict.get("power"),
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "power": self.power}
