from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class Seller(IDto, db.Model):
    __tablename__ = "seller"

    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    is_car_dealership_seller = Column(Integer, nullable=False)

    user = relationship(
        "User", back_populates="seller", primaryjoin="User.id == Seller.user_id"
    )
    car_dealerships = relationship("CarDealershipSeller", back_populates="seller")
    advertisements = relationship("Advertisement", back_populates="seller")

    def __repr__(self):
        return f"Seller(user_id={self.user_id}, is_car_dealership_seller={self.is_car_dealership_seller})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Seller:
        obj = Seller(
            user_id=dto_dict.get("user_id"),
            is_car_dealership_seller=dto_dict.get("is_car_dealership_seller"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "user_id": self.user_id,
            "is_car_dealership_seller": self.is_car_dealership_seller,
        }
