from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import motor_controller
from mydb.auth.domain.car.motor import Motor

motor_bp = Blueprint("motors", __name__, url_prefix="/motors/")


@motor_bp.get("")
def get_all_motors() -> Response:
    return make_response(jsonify(motor_controller.find_all()), HTTPStatus.OK)


@motor_bp.get('/<int:motor_id>')
def get_motors(motor_id: int) -> Response:
    return make_response(jsonify(motor_controller.find_by_id(motor_id)), HTTPStatus.OK)


@motor_bp.put('/<int:motor_id>')
def update_motor(motor_id: int) -> Response:
    content = request.get_json()
    motor = Motor.create_from_dto(content)
    motor_controller.update(motor_id, motor)
    return make_response("Motor updated", HTTPStatus.OK)


@motor_bp.patch('/<int:motor_id>')
def patch_motor(motor_id: int) -> Response:
    content = request.get_json()
    motor_controller.patch(motor_id, content)
    return make_response("Motor updated", HTTPStatus.OK)


@motor_bp.delete('/<int:motor_id>')
def delete_motor(motor_id: int) -> Response:
    motor_controller.delete(motor_id)
    return make_response("Motor deleted", HTTPStatus.OK)


@motor_bp.post("")
def create_motor() -> Response:
    content = request.get_json()
    motor = Motor.create_from_dto(content)
    motor_id = motor_controller.create(motor)
    return make_response(f"Motor created with ID: {motor_id}", HTTPStatus.CREATED)


@motor_bp.post("/bulk")
def create_all_motors() -> Response:
    content = request.get_json()
    motors = [Motor.create_from_dto(data) for data in content]
    motor_controller.create_all(motors)
    return make_response(motor_controller.create_all(motors), HTTPStatus.CREATED)


@motor_bp.delete("/all")
def delete_all_motors() -> Response:
    motor_controller.delete_all()
    return make_response("All Motors deleted", HTTPStatus.OK)

@motor_bp.get("cars/<int:id>")
def get_cars_with_car_types(id: int):
    return make_response(jsonify(motor_controller.get_cars(id)), HTTPStatus.OK)
