from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import car_dealership_controller
from mydb.auth.domain.car_dealership.car_dealership import CarDealership

car_dealership_bp = Blueprint("car_dealerships", __name__, url_prefix="/car_dealerships/")


@car_dealership_bp.get("")
def get_all_car_dealerships() -> Response:
    return make_response(jsonify(car_dealership_controller.find_all()), HTTPStatus.OK)


@car_dealership_bp.get('/<int:car_dealership_id>')
def get_car_dealerships(car_dealership_id: int) -> Response:
    return make_response(jsonify(car_dealership_controller.find_by_id(car_dealership_id)), HTTPStatus.OK)


@car_dealership_bp.put('/<int:car_dealership_id>')
def update_car_dealership(car_dealership_id: int) -> Response:
    content = request.get_json()
    car_dealership = CarDealership.create_from_dto(content)
    car_dealership_controller.update(car_dealership_id, car_dealership)
    return make_response("CarDealership updated", HTTPStatus.OK)


@car_dealership_bp.patch('/<int:car_dealership_id>')
def patch_car_dealership(car_dealership_id: int) -> Response:
    content = request.get_json()
    car_dealership_controller.patch(car_dealership_id, content)
    return make_response("CarDealership updated", HTTPStatus.OK)


@car_dealership_bp.delete('/<int:car_dealership_id>')
def delete_car_dealership(car_dealership_id: int) -> Response:
    car_dealership_controller.delete(car_dealership_id)
    return make_response("CarDealership deleted", HTTPStatus.OK)


@car_dealership_bp.post("")
def create_car_dealership() -> Response:
    content = request.get_json()
    car_dealership = CarDealership.create_from_dto(content)
    car_dealership_id = car_dealership_controller.create(car_dealership)
    return make_response(f"CarDealership created with ID: {car_dealership_id}", HTTPStatus.CREATED)


@car_dealership_bp.post("/bulk")
def create_all_car_dealerships() -> Response:
    content = request.get_json()
    car_dealerships = [CarDealership.create_from_dto(data) for data in content]
    car_dealership_controller.create_all(car_dealerships)
    return make_response(car_dealership_controller.create_all(car_dealerships), HTTPStatus.CREATED)


@car_dealership_bp.delete("/all")
def delete_all_car_dealerships() -> Response:
    car_dealership_controller.delete_all()
    return make_response("All CarDealerships deleted", HTTPStatus.OK)
