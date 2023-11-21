import logging
from http import HTTPStatus

from flask import Blueprint, Response, request, make_response, jsonify

from mydb.auth.controller import car_type_controller

car_bp = Blueprint("cars", __name__, url_prefix="/cars/")


@car_bp.get("")
def get_all_cars() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(car_type_controller.find_all()), HTTPStatus.OK)
