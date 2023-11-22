from __future__ import annotations

from typing import Any

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class TestDrive(IDto, db.Model):
    __tablename__ = "testdrive"

    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('car.id'), nullable=False)
    video_url = Column(String(100), nullable=False)

    car = relationship("Car", back_populates="testdrives")

    def __repr__(self):
        return f"TestDrive(id={self.id}, car_id={self.car_id}, video_url={self.video_url})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> TestDrive:
        obj = TestDrive(
            id=dto_dict.get("id"),
            car_id=dto_dict.get("car_id"),
            video_url=dto_dict.get("video_url"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {"id": self.id, "car_id": self.car_id, "video_url": self.video_url}
