from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class User(IDto, db.Model):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    surname = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)
    phone = Column(String(45))
    street_address = Column(String(45))
    gender = Column(String(25), nullable=False)
    city_name = Column(String(45), nullable=False)

    seller = relationship("Seller", back_populates="user", primaryjoin="User.id == Seller.user_id")
    comments = relationship("Comment", back_populates="user")
    car_dealerships = relationship("UserCarDealership", back_populates="user", primaryjoin="User.id == UserCarDealership.user_id")

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, surname={self.surname}, email={self.email}, " \
               f"phone={self.phone}, street_address={self.street_address}, gender={self.gender}, " \
               f"city_name={self.city_name})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> User:
        obj = User(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            email=dto_dict.get("email"),
            phone=dto_dict.get("phone"),
            street_address=dto_dict.get("street_address"),
            gender=dto_dict.get("gender"),
            city_name=dto_dict.get("city_name"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "phone": self.phone,
            "street_address": self.street_address,
            "gender": self.gender,
            "city_name": self.city_name,
        }
