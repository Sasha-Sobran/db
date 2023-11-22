from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class CarDealership(IDto, db.Model):
    __tablename__ = "car_dealership"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    street_address = Column(String(45), nullable=False)
    city_name = Column(String(45), nullable=False)
    site_url = Column(String(100))

    sellers = relationship("CarDealershipSeller", back_populates="car_dealership")
    advertisement = relationship("Advertisement", back_populates="car_dealership")
    user = relationship("User", back_populates="car_dealership")

    def __repr__(self):
        return f"CarDealership(id={self.id}, name={self.name}, email={self.email}, phone={self.phone}, " \
               f"street_address={self.street_address}, city_name={self.city_name}, site_url={self.site_url})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> CarDealership:
        obj = CarDealership(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
            email=dto_dict.get("email"),
            phone=dto_dict.get("phone"),
            street_address=dto_dict.get("street_address"),
            city_name=dto_dict.get("city_name"),
            site_url=dto_dict.get("site_url"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "street_address": self.street_address,
            "city_name": self.city_name,
            "site_url": self.site_url,
        }
