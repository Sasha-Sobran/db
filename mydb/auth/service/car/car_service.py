from http import HTTPStatus

from flask import abort

from mydb.auth.dao import car_dao
from mydb.auth.service.general_service import GeneralService


class CarService(GeneralService):
    _dao = car_dao

    def get_test_drives(self, id: int):
        car = self._dao.find_by_id(id)
        if car is None:
            abort(HTTPStatus.NOT_FOUND)
        return car.testdrives
