from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import car_dealership_seller_controller
from mydb.auth.domain.car_dealership.car_dealership_seller import CarDealershipSeller

car_dealership_seller_bp = Blueprint("car_dealership_sellers", __name__, url_prefix="/car_dealership_sellers/")


@car_dealership_seller_bp.get("")
def get_all_car_dealership_sellers() -> Response:
    return make_response(jsonify(car_dealership_seller_controller.find_all()), HTTPStatus.OK)


@car_dealership_seller_bp.get('/<int:car_dealership_seller_id>')
def get_car_dealership_sellers(car_dealership_seller_id: int) -> Response:
    return make_response(jsonify(car_dealership_seller_controller.find_by_id(car_dealership_seller_id)), HTTPStatus.OK)


@car_dealership_seller_bp.put('/<int:car_dealership_seller_id>')
def update_car_dealership_seller(car_dealership_seller_id: int) -> Response:
    content = request.get_json()
    car_dealership_seller = CarDealershipSeller.create_from_dto(content)
    car_dealership_seller_controller.update(car_dealership_seller_id, car_dealership_seller)
    return make_response("CarDealershipSeller updated", HTTPStatus.OK)


@car_dealership_seller_bp.patch('/<int:car_dealership_seller_id>')
def patch_car_dealership_seller(car_dealership_seller_id: int) -> Response:
    content = request.get_json()
    car_dealership_seller_controller.patch(car_dealership_seller_id, content)
    return make_response("CarDealershipSeller updated", HTTPStatus.OK)


@car_dealership_seller_bp.delete('/<int:car_dealership_seller_id>')
def delete_car_dealership_seller(car_dealership_seller_id: int) -> Response:
    car_dealership_seller_controller.delete(car_dealership_seller_id)
    return make_response("CarDealershipSeller deleted", HTTPStatus.OK)


@car_dealership_seller_bp.post("")
def create_car_dealership_seller() -> Response:
    content = request.get_json()
    car_dealership_seller = CarDealershipSeller.create_from_dto(content)
    car_dealership_seller_id = car_dealership_seller_controller.create(car_dealership_seller)
    return make_response(f"CarDealershipSeller created with ID: {car_dealership_seller_id}", HTTPStatus.CREATED)


@car_dealership_seller_bp.post("/bulk")
def create_all_car_dealership_sellers() -> Response:
    content = request.get_json()
    car_dealership_sellers = [CarDealershipSeller.create_from_dto(data) for data in content]
    car_dealership_seller_controller.create_all(car_dealership_sellers)
    return make_response(car_dealership_seller_controller.create_all(car_dealership_sellers), HTTPStatus.CREATED)


@car_dealership_seller_bp.delete("/all")
def delete_all_car_dealership_sellers() -> Response:
    car_dealership_seller_controller.delete_all()
    return make_response("All CarDealershipSellers deleted", HTTPStatus.OK)
