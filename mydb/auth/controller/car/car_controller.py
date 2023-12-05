from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import car_service


class CarController(GeneralController):
    _service = car_service

    def get_test_drives(self, id: int):
        return [
            test_drive.put_into_dto()
            for test_drive in self._service.get_test_drives(id)
        ]
