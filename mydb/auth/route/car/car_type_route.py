from http import HTTPStatus

from flask import Blueprint, Response, request, make_response, jsonify

from mydb.auth.controller import car_type_controller
from mydb.auth.domain.car.car_type import CarType

car_type_bp = Blueprint("cars", __name__, url_prefix="/car_types/")


@car_type_bp.get("")
def get_all_car_types() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(car_type_controller.find_all()), HTTPStatus.OK)


@car_type_bp.get('/<int:car_type_id>')
def get_car_types(car_type_id: int) -> Response:
    """
    Gets car_type by ID.
    :return: Response object
    """
    return make_response(jsonify(car_type_controller.find_by_id(car_type_id)), HTTPStatus.OK)


@car_type_bp.put('/<int:car_type_id>')
def update_car_type(car_type_id: int) -> Response:
    """
    Updates car_type by ID.
    :return: Response object
    """
    content = request.get_json()
    car_type = CarType.create_from_dto(content)
    car_type_controller.update(car_type_id, car_type)
    return make_response("CarType updated", HTTPStatus.OK)


@car_type_bp.patch('/<int:car_type_id>')
def patch_car_type(car_type_id: int) -> Response:
    """
    Patches car_type by ID.
    :return: Response object
    """
    content = request.get_json()
    car_type_controller.patch(car_type_id, content)
    return make_response("CarType updated", HTTPStatus.OK)


@car_type_bp.delete('/<int:car_type_id>')
def delete_car_type(car_type_id: int) -> Response:
    """
    Deletes car_type by ID.
    :return: Response object
    """
    car_type_controller.delete(car_type_id)
    return make_response("CarType deleted", HTTPStatus.OK)
