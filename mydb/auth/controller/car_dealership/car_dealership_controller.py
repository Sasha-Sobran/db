from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import car_dealership_service


class CarDealershipController(GeneralController):
    _service = car_dealership_service
