from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class Image(IDto, db.Model):
    __tablename__ = "image"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(100), nullable=False)
    advertisement_id = Column(Integer, ForeignKey('advertisement.id'), nullable=False)

    advertisement = relationship("Advertisement", back_populates="images")

    def __repr__(self):
        return f"Image(id={self.id}, url={self.url}, advertisement_id={self.advertisement_id})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Image:
        obj = Image(
            id=dto_dict.get("id"),
            url=dto_dict.get("url"),
            advertisement_id=dto_dict.get("advertisement_id"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "url": self.url,
            "advertisement_id": self.advertisement_id,
        }
