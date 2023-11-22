from http import HTTPStatus

from flask import abort

from mydb.auth.dao import advertisement_dao, user_dao
from mydb.auth.service.general_service import GeneralService


class AdvertisementService(GeneralService):
    _dao = advertisement_dao

    def get_comments(self, id: int):
        advertisement = self._dao.find_by_id(id)
        if advertisement is None:
            abort(HTTPStatus.NOT_FOUND)

        comments = [{"comment text": comment.text, "user": user_dao.find_by_id(comment.user_id).name} for comment in
                    advertisement.comments]
        return comments

    def get_images(self, id):
        advertisement = self._dao.find_by_id(id)
        if advertisement is None:
            abort(HTTPStatus.NOT_FOUND)

        return advertisement.images
