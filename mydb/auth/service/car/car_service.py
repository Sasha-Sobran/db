from mydb.auth.dao import car_dao
from mydb.auth.service.general_service import GeneralService


class CarService(GeneralService):
    _dao = car_dao
