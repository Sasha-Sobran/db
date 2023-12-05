from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class UserCarDealership(IDto, db.Model):
    __tablename__ = "user_car_dealership"

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, primary_key=True)
    car_dealership_id = Column(Integer, ForeignKey('car_dealership.id'), nullable=False, primary_key=True)

    user = relationship("User", back_populates="car_dealerships")
    car_dealership = relationship("CarDealership", back_populates="users")

    def __repr__(self):
        return f"UserCarDealership(user_id={self.user_id}, car_dealership_id={self.car_dealership_id})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> UserCarDealership:
        obj = UserCarDealership(
            user_id=dto_dict.get("user_id"),
            car_dealership_id=dto_dict.get("car_dealership_id"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "user_id": self.user_id,
            "car_dealership_id": self.car_dealership_id,
        }
