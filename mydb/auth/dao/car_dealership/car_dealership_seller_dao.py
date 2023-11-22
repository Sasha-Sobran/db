from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.car_dealership.car_dealership_seller import CarDealershipSeller


class CarDealershipSellerDao(GeneralDAO):
    _domain_type = CarDealershipSeller
