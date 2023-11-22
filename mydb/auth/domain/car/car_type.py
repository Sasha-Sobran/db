from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class CarType(db.Model, IDto):
    __tablename__ = "car_type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)

    cars = relationship("Car", back_populates="car_type")

    def __repr__(self):
        return f"CarType(id={self.id}, name={self.name})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> CarType:
        obj = CarType(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {"id": self.id, "name": self.name}
