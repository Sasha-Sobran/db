from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import car_type_service


class CarTypeController(GeneralController):
    _service = car_type_service
