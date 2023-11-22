from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class CarDealershipSeller(IDto, db.Model):
    __tablename__ = "car_dealership_seller"

    car_dealership_user_id = Column(Integer, ForeignKey('car_dealership.id'), nullable=False)
    seller_user_id = Column(Integer, ForeignKey('seller.user_id'), nullable=False, primary_key=True)

    car_dealership = relationship("CarDealership", back_populates="sellers")
    seller = relationship("Seller", back_populates="car_dealerships")

    def __repr__(self):
        return f"CarDealershipSeller(car_dealership_user_id={self.car_dealership_user_id}, " \
               f"seller_user_id={self.seller_user_id})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> CarDealershipSeller:
        obj = CarDealershipSeller(
            car_dealership_user_id=dto_dict.get("car_dealership_user_id"),
            seller_user_id=dto_dict.get("seller_user_id"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "car_dealership_user_id": self.car_dealership_user_id,
            "seller_user_id": self.seller_user_id,
        }
