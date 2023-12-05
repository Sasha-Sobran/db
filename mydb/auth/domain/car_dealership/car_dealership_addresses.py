from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class CarDealershipAddresses(IDto, db.Model):
    __tablename__ = "car_dealership_addresses"

    car_dealership_id = Column(Integer, nullable=False, primary_key=True)
    street_address = Column(String(45), nullable=False)
    city_name = Column(String(45), nullable=False)

    def __repr__(self):
        return (
            f"UserCarDealership(car_dealership_id={self.car_dealership_id}, street_address={self.street_address},"
            f" city_name={self.city_name})"
        )

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> CarDealershipAddresses:
        obj = CarDealershipAddresses(
            car_dealership_id=dto_dict.get("car_dealership_id"),
            street_address=dto_dict.get("street_address"),
            city_name=dto_dict.get("city_name"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "car_dealership_id": self.car_dealership_id,
            "street_address": self.street_address,
            "city_name": self.city_name,
        }
