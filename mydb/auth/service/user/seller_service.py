from http import HTTPStatus
from flask import abort

from mydb.auth.dao import seller_dao
from mydb.auth.service.general_service import GeneralService


class SellerService(GeneralService):
    _dao = seller_dao

    def get_advertisements(self, id: int):
        seller = self._dao.find_by_id(id)
        if seller is None:
            abort(HTTPStatus.NOT_FOUND)

        return seller.advertisements
