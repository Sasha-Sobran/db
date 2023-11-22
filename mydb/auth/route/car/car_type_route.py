from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import car_type_controller
from mydb.auth.domain.car.car_type import CarType

car_type_bp = Blueprint("car_types", __name__, url_prefix="/car_types/")


@car_type_bp.get("")
def get_all_car_types() -> Response:
    return make_response(jsonify(car_type_controller.find_all()), HTTPStatus.OK)


@car_type_bp.get('/<int:car_type_id>')
def get_car_types(car_type_id: int) -> Response:
    return make_response(jsonify(car_type_controller.find_by_id(car_type_id)), HTTPStatus.OK)


@car_type_bp.put('/<int:car_type_id>')
def update_car_type(car_type_id: int) -> Response:
    content = request.get_json()
    car_type = CarType.create_from_dto(content)
    car_type_controller.update(car_type_id, car_type)
    return make_response("CarType updated", HTTPStatus.OK)


@car_type_bp.patch('/<int:car_type_id>')
def patch_car_type(car_type_id: int) -> Response:
    content = request.get_json()
    car_type_controller.patch(car_type_id, content)
    return make_response("CarType updated", HTTPStatus.OK)


@car_type_bp.delete('/<int:car_type_id>')
def delete_car_type(car_type_id: int) -> Response:
    car_type_controller.delete(car_type_id)
    return make_response("CarType deleted", HTTPStatus.OK)


@car_type_bp.post("")
def create_car_type() -> Response:
    content = request.get_json()
    car_type = CarType.create_from_dto(content)
    car_type_id = car_type_controller.create(car_type)
    return make_response(f"CarType created with ID: {car_type_id}", HTTPStatus.CREATED)


@car_type_bp.post("/bulk")
def create_all_car_types() -> Response:
    content = request.get_json()
    car_types = [CarType.create_from_dto(data) for data in content]
    car_type_controller.create_all(car_types)
    return make_response(car_type_controller.create_all(car_types), HTTPStatus.CREATED)


@car_type_bp.delete("/all")
def delete_all_car_types() -> Response:
    car_type_controller.delete_all()
    return make_response("All CarTypes deleted", HTTPStatus.OK)
