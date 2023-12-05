from http import HTTPStatus

from flask import abort

from mydb.auth.dao import (
    car_dealership_seller_dao,
    seller_dao,
    user_dao,
    car_dealership_dao,
)
from mydb.auth.service.general_service import GeneralService


class CarDealershipSellerService(GeneralService):
    _dao = car_dealership_seller_dao

    def seller_car_dealerships(self):
        car_dealership_sellers = self._dao.find_all()
        result = {}

        for car_dealership_seller in car_dealership_sellers:
            seller_id = car_dealership_seller.seller_user_id
            if seller_id not in result:
                seller = seller_dao.find_by_id(seller_id)
                result[seller_id] = {
                    user_dao.find_by_id(seller.user_id).name: [
                        car_dealership_dao.find_by_id(
                            obj.car_dealership_id
                        ).put_into_dto()
                        for obj in seller.car_dealerships
                    ]
                }

        return list(result.values())

    def car_dealership_seller(self):
        car_dealership_sellers = self._dao.find_all()
        if not car_dealership_sellers:
            abort(HTTPStatus.NOT_FOUND)
        result = {}
        for car_dealership_seller in car_dealership_sellers:
            car_dealership_id = car_dealership_seller.car_dealership_id
            if car_dealership_id not in result:
                car_dealership = car_dealership_dao.find_by_id(car_dealership_id)
                result[car_dealership_id] = {
                    car_dealership.name: seller_dao.find_by_id(
                        obj.seller_user_id
                    ).put_into_dto()
                    for obj in car_dealership.sellers
                }
        return list(result.values())
