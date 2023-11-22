from mydb.auth.dao import car_dealership_seller_dao
from mydb.auth.service.general_service import GeneralService


class CarDealershipSellerService(GeneralService):
    _dao = car_dealership_seller_dao
