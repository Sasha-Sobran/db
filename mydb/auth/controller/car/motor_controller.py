from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import motor_service


class MotorController(GeneralController):
    _service = motor_service

    def get_cars(self, id):
        return [car.put_into_dto() for car in self._service.get_cars(id)]
