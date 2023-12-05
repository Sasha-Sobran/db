from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.car_dealership.car_dealership import CarDealership


class CarDealershipDao(GeneralDAO):
    _domain_type = CarDealership
