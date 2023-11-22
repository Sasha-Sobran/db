from http import HTTPStatus
from os import abort

from mydb.auth.dao import car_dealership_dao
from mydb.auth.service.general_service import GeneralService


class CarDealershipService(GeneralService):
    _dao = car_dealership_dao
