from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import image_controller
from mydb.auth.domain.advertisement.image import Image

image_bp = Blueprint("images", __name__, url_prefix="/images/")


@image_bp.get("")
def get_all_images() -> Response:
    return make_response(jsonify(image_controller.find_all()), HTTPStatus.OK)


@image_bp.get("/<int:image_id>")
def get_images(image_id: int) -> Response:
    return make_response(jsonify(image_controller.find_by_id(image_id)), HTTPStatus.OK)


@image_bp.put("/<int:image_id>")
def update_image(image_id: int) -> Response:
    content = request.get_json()
    image = Image.create_from_dto(content)
    image_controller.update(image_id, image)
    return make_response("Image updated", HTTPStatus.OK)


@image_bp.patch("/<int:image_id>")
def patch_image(image_id: int) -> Response:
    content = request.get_json()
    image_controller.patch(image_id, content)
    return make_response("Image updated", HTTPStatus.OK)


@image_bp.delete("/<int:image_id>")
def delete_image(image_id: int) -> Response:
    image_controller.delete(image_id)
    return make_response("Image deleted", HTTPStatus.OK)


@image_bp.post("")
def create_image() -> Response:
    content = request.get_json()
    image = Image.create_from_dto(content)
    image_id = image_controller.create(image)
    return make_response(f"Image created with ID: {image_id}", HTTPStatus.CREATED)


@image_bp.post("/bulk")
def create_all_images() -> Response:
    content = request.get_json()
    images = [Image.create_from_dto(data) for data in content]
    image_controller.create_all(images)
    return make_response(image_controller.create_all(images), HTTPStatus.CREATED)


@image_bp.delete("/all")
def delete_all_images() -> Response:
    image_controller.delete_all()
    return make_response("All Images deleted", HTTPStatus.OK)
