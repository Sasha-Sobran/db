from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import test_drive_controller
from mydb.auth.domain.car.test_drive import TestDrive

test_drive_bp = Blueprint("test_drives", __name__, url_prefix="/test_drives/")


@test_drive_bp.get("")
def get_all_test_drives() -> Response:
    return make_response(jsonify(test_drive_controller.find_all()), HTTPStatus.OK)


@test_drive_bp.get("/<int:test_drive_id>")
def get_test_drives(test_drive_id: int) -> Response:
    return make_response(
        jsonify(test_drive_controller.find_by_id(test_drive_id)), HTTPStatus.OK
    )


@test_drive_bp.put("/<int:test_drive_id>")
def update_test_drive(test_drive_id: int) -> Response:
    content = request.get_json()
    test_drive = TestDrive.create_from_dto(content)
    test_drive_controller.update(test_drive_id, test_drive)
    return make_response("TestDrive updated", HTTPStatus.OK)


@test_drive_bp.patch("/<int:test_drive_id>")
def patch_test_drive(test_drive_id: int) -> Response:
    content = request.get_json()
    test_drive_controller.patch(test_drive_id, content)
    return make_response("TestDrive updated", HTTPStatus.OK)


@test_drive_bp.delete("/<int:test_drive_id>")
def delete_test_drive(test_drive_id: int) -> Response:
    test_drive_controller.delete(test_drive_id)
    return make_response("TestDrive deleted", HTTPStatus.OK)


@test_drive_bp.post("")
def create_test_drive() -> Response:
    content = request.get_json()
    test_drive = TestDrive.create_from_dto(content)
    test_drive_id = test_drive_controller.create(test_drive)
    return make_response(
        f"TestDrive created with ID: {test_drive_id}", HTTPStatus.CREATED
    )


@test_drive_bp.post("/bulk")
def create_all_test_drives() -> Response:
    content = request.get_json()
    test_drives = [TestDrive.create_from_dto(data) for data in content]
    test_drive_controller.create_all(test_drives)
    return make_response(
        test_drive_controller.create_all(test_drives), HTTPStatus.CREATED
    )


@test_drive_bp.delete("/all")
def delete_all_test_drives() -> Response:
    test_drive_controller.delete_all()
    return make_response("All TestDrives deleted", HTTPStatus.OK)
