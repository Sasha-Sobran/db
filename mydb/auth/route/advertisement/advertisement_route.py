from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from mydb import db
from mydb.auth.controller import advertisement_controller
from mydb.auth.domain.advertisement.advertisement import Advertisement

advertisement_bp = Blueprint("advertisements", __name__, url_prefix="/advertisements/")


@advertisement_bp.get("")
def get_all_advertisements() -> Response:
    return make_response(jsonify(advertisement_controller.find_all()), HTTPStatus.OK)


@advertisement_bp.get('/<int:advertisement_id>')
def get_advertisements(advertisement_id: int) -> Response:
    return make_response(jsonify(advertisement_controller.find_by_id(advertisement_id)), HTTPStatus.OK)


@advertisement_bp.put('/<int:advertisement_id>')
def update_advertisement(advertisement_id: int) -> Response:
    content = request.get_json()
    advertisement = Advertisement.create_from_dto(content)
    advertisement_controller.update(advertisement_id, advertisement)
    return make_response("Advertisement updated", HTTPStatus.OK)


@advertisement_bp.patch('/<int:advertisement_id>')
def patch_advertisement(advertisement_id: int) -> Response:
    content = request.get_json()
    advertisement_controller.patch(advertisement_id, content)
    return make_response("Advertisement updated", HTTPStatus.OK)


@advertisement_bp.delete('/<int:advertisement_id>')
def delete_advertisement(advertisement_id: int) -> Response:
    advertisement_controller.delete(advertisement_id)
    return make_response("Advertisement deleted", HTTPStatus.OK)


@advertisement_bp.post("")
def create_advertisement() -> Response:
    content = request.get_json()
    advertisement = Advertisement.create_from_dto(content)
    advertisement_id = advertisement_controller.create(advertisement)
    return make_response(f"Advertisement created with ID: {advertisement_id}", HTTPStatus.CREATED)


@advertisement_bp.post("/bulk")
def create_all_advertisements() -> Response:
    content = request.get_json()
    advertisements = [Advertisement.create_from_dto(data) for data in content]
    advertisement_controller.create_all(advertisements)
    return make_response(advertisement_controller.create_all(advertisements), HTTPStatus.CREATED)


@advertisement_bp.delete("/all")
def delete_all_advertisements() -> Response:
    advertisement_controller.delete_all()
    return make_response("All Advertisements deleted", HTTPStatus.OK)


@advertisement_bp.get("/comments/<int:advertisement_id>")
def get_advertisement_comments(advertisement_id):
    return make_response(jsonify(advertisement_controller.get_comments(advertisement_id)), HTTPStatus.OK)

@advertisement_bp.get("/images/<int:advertisement_id>")
def get_advertisement_images(advertisement_id):
    return make_response(jsonify(advertisement_controller.get_images(advertisement_id)), HTTPStatus.OK)
