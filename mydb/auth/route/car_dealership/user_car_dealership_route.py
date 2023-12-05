from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import user_car_dealership_controller
from mydb.auth.domain.car_dealership.user_cardealership import UserCarDealership

user_car_dealership_bp = Blueprint("user_car_dealerships", __name__, url_prefix="/user_car_dealerships/")


@user_car_dealership_bp.get("")
def get_all_user_car_dealerships() -> Response:
    return make_response(jsonify(user_car_dealership_controller.find_all()), HTTPStatus.OK)


@user_car_dealership_bp.get('/<int:user_car_dealership_id>')
def get_user_car_dealerships(user_car_dealership_id: int) -> Response:
    return make_response(jsonify(user_car_dealership_controller.find_by_id(user_car_dealership_id)), HTTPStatus.OK)


@user_car_dealership_bp.put('/<int:user_car_dealership_id>')
def update_user_car_dealership(user_car_dealership_id: int) -> Response:
    content = request.get_json()
    user_car_dealership = UserCarDealership.create_from_dto(content)
    user_car_dealership_controller.update(user_car_dealership_id, user_car_dealership)
    return make_response("UserCarDealership updated", HTTPStatus.OK)


@user_car_dealership_bp.patch('/<int:user_car_dealership_id>')
def patch_user_car_dealership(user_car_dealership_id: int) -> Response:
    content = request.get_json()
    user_car_dealership_controller.patch(user_car_dealership_id, content)
    return make_response("UserCarDealership updated", HTTPStatus.OK)


@user_car_dealership_bp.delete('/<int:user_car_dealership_id>')
def delete_user_car_dealership(user_car_dealership_id: int) -> Response:
    user_car_dealership_controller.delete(user_car_dealership_id)
    return make_response("UserCarDealership deleted", HTTPStatus.OK)


@user_car_dealership_bp.post("")
def create_user_car_dealership() -> Response:
    content = request.get_json()
    user_car_dealership = UserCarDealership.create_from_dto(content)
    user_car_dealership_id = user_car_dealership_controller.create(user_car_dealership)
    return make_response(f"UserCarDealership created with ID: {user_car_dealership_id}", HTTPStatus.CREATED)


@user_car_dealership_bp.post("/bulk")
def create_all_user_car_dealerships() -> Response:
    content = request.get_json()
    user_car_dealerships = [UserCarDealership.create_from_dto(data) for data in content]
    user_car_dealership_controller.create_all(user_car_dealerships)
    return make_response(user_car_dealership_controller.create_all(user_car_dealerships), HTTPStatus.CREATED)


@user_car_dealership_bp.delete("/all")
def delete_all_user_car_dealerships() -> Response:
    user_car_dealership_controller.delete_all()
    return make_response("All UserCarDealerships deleted", HTTPStatus.OK)


@user_car_dealership_bp.get("/user_car_dealerships")
def user_car_dealerships():
    return make_response(jsonify(user_car_dealership_controller.user_car_dealerships()), HTTPStatus.OK)


@user_car_dealership_bp.get("/car_dealerships_user")
def car_dealerships_user():
    return make_response(jsonify(user_car_dealership_controller.car_dealerships_user()), HTTPStatus.OK)
