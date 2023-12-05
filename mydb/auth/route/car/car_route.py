from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import car_controller
from mydb.auth.domain.car.car import Car

car_bp = Blueprint("cars", __name__, url_prefix="/cars/")


@car_bp.get("")
def get_all_cars() -> Response:
    return make_response(jsonify(car_controller.find_all()), HTTPStatus.OK)


@car_bp.get('/<int:car_id>')
def get_cars(car_id: int) -> Response:
    return make_response(jsonify(car_controller.find_by_id(car_id)), HTTPStatus.OK)


@car_bp.put('/<int:car_id>')
def update_car(car_id: int) -> Response:
    content = request.get_json()
    car = Car.create_from_dto(content)
    car_controller.update(car_id, car)
    return make_response("Car updated", HTTPStatus.OK)


@car_bp.patch('/<int:car_id>')
def patch_car(car_id: int) -> Response:
    content = request.get_json()
    car_controller.patch(car_id, content)
    return make_response("Car updated", HTTPStatus.OK)


@car_bp.delete('/<int:car_id>')
def delete_car(car_id: int) -> Response:
    car_controller.delete(car_id)
    return make_response("Car deleted", HTTPStatus.OK)


@car_bp.post("")
def create_car() -> Response:
    content = request.get_json()
    car = Car.create_from_dto(content)
    car_id = car_controller.create(car)
    return make_response(f"Car created with ID: {car_id}", HTTPStatus.CREATED)


@car_bp.post("/bulk")
def create_all_cars() -> Response:
    content = request.get_json()
    cars = [Car.create_from_dto(data) for data in content]
    car_controller.create_all(cars)
    return make_response(car_controller.create_all(cars), HTTPStatus.CREATED)


@car_bp.delete("/all")
def delete_all_cars() -> Response:
    car_controller.delete_all()
    return make_response("All Cars deleted", HTTPStatus.OK)


@car_bp.get("test_drives/<int:car_id>")
def get_car_test_drives(car_id):
    return make_response(jsonify(car_controller.get_test_drives(car_id)), HTTPStatus.OK)
