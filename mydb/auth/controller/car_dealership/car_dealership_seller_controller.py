from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import car_dealership_seller_service


class CarDealershipSellerController(GeneralController):
    _service = car_dealership_seller_service
