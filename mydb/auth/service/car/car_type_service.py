from http import HTTPStatus

from flask import abort

from mydb.auth.dao import car_type_dao
from mydb.auth.service.general_service import GeneralService


class CarTypeService(GeneralService):
    _dao = car_type_dao

    def get_cars(self, id: int):
        car_type = self._dao.find_by_id(id)
        if car_type is None:
            abort(HTTPStatus.NOT_FOUND)
        return car_type.cars
