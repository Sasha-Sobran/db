from mydb.auth.dao import car_type_dao
from mydb.auth.service.general_service import GeneralService


class CarTypeService(GeneralService):
    _dao = car_type_dao
