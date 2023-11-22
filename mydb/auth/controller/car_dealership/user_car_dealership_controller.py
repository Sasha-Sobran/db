from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import user_car_dealership_service


class UserCarDealershipController(GeneralController):
    _service = user_car_dealership_service
