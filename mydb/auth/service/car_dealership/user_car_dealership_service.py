from http import HTTPStatus

from flask import abort

from mydb.auth.dao import user_car_dealership_dao, car_dealership_dao, user_dao
from mydb.auth.service.general_service import GeneralService


class UserCarDealershipService(GeneralService):
    _dao = user_car_dealership_dao

    def user_car_dealerships(self):
        user_car_dealerships = self._dao.find_all()
        result = {}

        for user_car_dealership in user_car_dealerships:
            user_id = user_car_dealership.user_id
            if user_id not in result:
                user = user_dao.find_by_id(user_id)
                result[user_id] = {
                    user.name: [
                        car_dealership_dao.find_by_id(
                            obj.car_dealership_id
                        ).put_into_dto()
                        for obj in user.car_dealerships
                    ]
                }

        return list(result.values())

    def car_dealership_user(self):
        user_car_dealerships = self._dao.find_all()
        result = {}

        for user_car_dealership in user_car_dealerships:
            car_dealership_id = user_car_dealership.car_dealership_id
            if car_dealership_id not in result:
                car_dealership = car_dealership_dao.find_by_id(car_dealership_id)
                result[car_dealership_id] = {
                    car_dealership.name: [
                        user_dao.find_by_id(obj.user_id).put_into_dto()
                        for obj in car_dealership.users
                    ]
                }

        return list(result.values())

    def insert_user_car_dealership(self, user_name: str, car_dealership_name: str):
        self._dao.insert_user_car_dealership(user_name, car_dealership_name)
