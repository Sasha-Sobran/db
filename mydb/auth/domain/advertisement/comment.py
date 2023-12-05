from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class Comment(IDto, db.Model):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, autoincrement=True)
    advertisement_id = Column(Integer, ForeignKey('advertisement.id'), nullable=False)
    text = Column(String(150), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    advertisement = relationship("Advertisement", back_populates="comments")
    user = relationship("User", back_populates="comments")

    def __repr__(self):
        return f"Comment(id={self.id}, advertisement_id={self.advertisement_id}, text={self.text}, " \
               f"user_id={self.user_id})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Comment:
        obj = Comment(
            id=dto_dict.get("id"),
            advertisement_id=dto_dict.get("advertisement_id"),
            text=dto_dict.get("text"),
            user_id=dto_dict.get("user_id"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "advertisement_id": self.advertisement_id,
            "text": self.text,
            "user_id": self.user_id,
        }
