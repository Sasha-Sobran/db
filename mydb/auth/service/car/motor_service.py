from http import HTTPStatus

from flask import abort

from mydb.auth.dao import motor_dao
from mydb.auth.service.general_service import GeneralService


class MotorService(GeneralService):
    _dao = motor_dao

    def get_cars(self, id: int):
        motor = self._dao.find_by_id(id)
        if motor is None:
            abort(HTTPStatus.NOT_FOUND)
        return motor.cars
