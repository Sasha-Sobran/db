from __future__ import annotations

from typing import Any

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class Car(IDto, db.Model):
    __tablename__ = "car"

    id = Column(Integer, primary_key=True, autoincrement=True)
    brand_name = Column(String(30), nullable=False)
    lifted_weight = Column(Integer, nullable=False)
    car_type_id = Column(Integer, ForeignKey('car_type.id'), nullable=False)
    motor_id = Column(Integer, ForeignKey('motor.id'), nullable=False)

    car_type = relationship("CarType", back_populates="cars")
    motor = relationship("Motor", back_populates="cars")
    testdrives = relationship("TestDrive", back_populates="car")
    advertisement = relationship("Advertisement", back_populates="car")

    def __repr__(self):
        return f"Car(id={self.id}, brand_name={self.brand_name}, lifted_weight={self.lifted_weight}, " \
               f"car_type_id={self.car_type_id}, motor_id={self.motor_id})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Car:
        obj = Car(
            id=dto_dict.get("id"),
            brand_name=dto_dict.get("brand_name"),
            lifted_weight=dto_dict.get("lifted_weight"),
            car_type_id=dto_dict.get("car_type_id"),
            motor_id=dto_dict.get("motor_id"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "brand_name": self.brand_name,
            "lifted_weight": self.lifted_weight,
            "car_type_id": self.car_type_id,
            "motor_id": self.motor_id,
        }
