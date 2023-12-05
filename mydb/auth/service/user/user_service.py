from http import HTTPStatus

from flask import abort

from mydb.auth.dao import user_dao
from mydb.auth.service.general_service import GeneralService


class UserService(GeneralService):
    _dao = user_dao

    def get_comments(self, id: int):
        user = self._dao.find_by_id(id)
        if user is None:
            abort(HTTPStatus.NOT_FOUND)

        comments = [
            {"comment text": comment.text, "user": self._dao.find_by_id(id).name}
            for comment in user.comments
        ]
        return comments
