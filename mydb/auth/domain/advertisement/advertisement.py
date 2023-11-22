from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class Advertisement(IDto, db.Model):
    __tablename__ = "advertisement"

    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('car.id'), nullable=False)
    price = Column(DECIMAL, nullable=False)
    car_dealership_id = Column(Integer, ForeignKey('car_dealership.id'), nullable=False)
    seller_id = Column(Integer, ForeignKey('seller.user_id'), nullable=False)

    car = relationship("Car", back_populates="advertisement")
    car_dealership = relationship("CarDealership", back_populates="advertisement")
    seller = relationship("Seller", back_populates="advertisements")
    images = relationship("Image", back_populates="advertisement")
    comments = relationship("Comment", back_populates="advertisement")

    def __repr__(self):
        return f"Advertisement(id={self.id}, car_id={self.car_id}, price={self.price}, " \
               f"car_dealership_id={self.car_dealership_id}, seller_id={self.seller_id})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Advertisement:
        obj = Advertisement(
            id=dto_dict.get("id"),
            car_id=dto_dict.get("car_id"),
            price=dto_dict.get("price"),
            car_dealership_id=dto_dict.get("car_dealership_id"),
            seller_id=dto_dict.get("seller_id"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "car_id": self.car_id,
            "price": self.price,
            "car_dealership_id": self.car_dealership_id,
            "seller_id": self.seller_id,
        }
