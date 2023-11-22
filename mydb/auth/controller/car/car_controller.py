from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import car_service


class CarController(GeneralController):
    _service = car_service
