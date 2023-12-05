from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import car_dealership_addresses_controller
from mydb.auth.domain.car_dealership.car_dealership_addresses import (
    CarDealershipAddresses,
)

car_dealership_addresses_bp = Blueprint(
    "car_dealership_addresses", __name__, url_prefix="/car_dealership_addresses"
)


@car_dealership_addresses_bp.get("")
def get_all_car_dealership_addresses() -> Response:
    return make_response(
        jsonify(car_dealership_addresses_controller.find_all()), HTTPStatus.OK
    )


@car_dealership_addresses_bp.get("/<int:car_dealership_addresses_id>")
def get_car_dealership_addresses(car_dealership_addresses_id: int) -> Response:
    return make_response(
        jsonify(
            car_dealership_addresses_controller.find_by_id(car_dealership_addresses_id)
        ),
        HTTPStatus.OK,
    )


@car_dealership_addresses_bp.put("/<int:car_dealership_addresses_id>")
def update_car_dealership_addresses(car_dealership_addresses_id: int) -> Response:
    content = request.get_json()
    car_dealership_addresses = CarDealershipAddresses.create_from_dto(content)
    car_dealership_addresses_controller.update(
        car_dealership_addresses_id, car_dealership_addresses
    )
    return make_response("CarDealershipAddress updated", HTTPStatus.OK)


@car_dealership_addresses_bp.patch("/<int:car_dealership_addresses_id>")
def patch_car_dealership_addresses(car_dealership_addresses_id: int) -> Response:
    content = request.get_json()
    car_dealership_addresses_controller.patch(car_dealership_addresses_id, content)
    return make_response("CarDealershipAddress updated", HTTPStatus.OK)


@car_dealership_addresses_bp.delete("/<int:car_dealership_addresses_id>")
def delete_car_dealership_addresses(car_dealership_addresses_id: int) -> Response:
    car_dealership_addresses_controller.delete(car_dealership_addresses_id)
    return make_response("CarDealershipAddress deleted", HTTPStatus.OK)


@car_dealership_addresses_bp.post("")
def create_car_dealership_addresses() -> Response:
    content = request.get_json()
    print(content)
    car_dealership_addresses = CarDealershipAddresses.create_from_dto(content)
    car_dealership_addresses_id = car_dealership_addresses_controller.create(
        car_dealership_addresses
    )
    return make_response(
        f"CarDealershipAddress created with ID: {car_dealership_addresses_id}",
        HTTPStatus.CREATED,
    )


@car_dealership_addresses_bp.post("/bulk")
def create_all_car_dealership_addresses() -> Response:
    content = request.get_json()
    car_dealership_addresses = [
        CarDealershipAddresses.create_from_dto(data) for data in content
    ]
    car_dealership_addresses_controller.create_all(car_dealership_addresses)
    return make_response(
        car_dealership_addresses_controller.create_all(car_dealership_addresses),
        HTTPStatus.CREATED,
    )


@car_dealership_addresses_bp.delete("/all")
def delete_all_car_dealership_addresses() -> Response:
    car_dealership_addresses_controller.delete_all()
    return make_response("All CarDealershipAddress deleted", HTTPStatus.OK)
