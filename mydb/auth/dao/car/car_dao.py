from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.car.car import Car


class CarDao(GeneralDAO):
    _domain_type = Car
