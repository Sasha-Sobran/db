from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import user_car_dealership_service


class UserCarDealershipController(GeneralController):
    _service = user_car_dealership_service

    def user_car_dealerships(self):
        return [obj for obj in self._service.user_car_dealerships()]

    def car_dealerships_user(self):
        return [obj for obj in self._service.car_dealership_user()]

    def insert_user_car_dealership(self, user_name: str, car_dealership_name: str):
        self._service.insert_user_car_dealership(user_name, car_dealership_name)
