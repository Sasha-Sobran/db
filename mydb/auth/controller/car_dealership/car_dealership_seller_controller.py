from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import car_dealership_seller_service


class CarDealershipSellerController(GeneralController):
    _service = car_dealership_seller_service

    def seller_car_dealerships(self):
        return [obj for obj in self._service.seller_car_dealerships()]

    def car_dealerships_seller(self):
        return [obj for obj in self._service.car_dealership_seller()]
