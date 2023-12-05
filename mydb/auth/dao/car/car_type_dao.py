from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.car.car_type import CarType


class CarTypeDao(GeneralDAO):
    _domain_type = CarType
