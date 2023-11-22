from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import motor_service


class MotorController(GeneralController):
    _service = motor_service
