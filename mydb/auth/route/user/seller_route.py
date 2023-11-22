from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import seller_controller
from mydb.auth.domain.user.seller import Seller

seller_bp = Blueprint("sellers", __name__, url_prefix="/sellers/")


@seller_bp.get("")
def get_all_sellers() -> Response:
    return make_response(jsonify(seller_controller.find_all()), HTTPStatus.OK)


@seller_bp.get('/<int:seller_id>')
def get_sellers(seller_id: int) -> Response:
    return make_response(jsonify(seller_controller.find_by_id(seller_id)), HTTPStatus.OK)


@seller_bp.put('/<int:seller_id>')
def update_seller(seller_id: int) -> Response:
    content = request.get_json()
    seller = Seller.create_from_dto(content)
    seller_controller.update(seller_id, seller)
    return make_response("Seller updated", HTTPStatus.OK)


@seller_bp.patch('/<int:seller_id>')
def patch_seller(seller_id: int) -> Response:
    content = request.get_json()
    seller_controller.patch(seller_id, content)
    return make_response("Seller updated", HTTPStatus.OK)


@seller_bp.delete('/<int:seller_id>')
def delete_seller(seller_id: int) -> Response:
    seller_controller.delete(seller_id)
    return make_response("Seller deleted", HTTPStatus.OK)


@seller_bp.post("")
def create_seller() -> Response:
    content = request.get_json()
    seller = Seller.create_from_dto(content)
    seller_id = seller_controller.create(seller)
    return make_response(f"Seller created with ID: {seller_id}", HTTPStatus.CREATED)


@seller_bp.post("/bulk")
def create_all_sellers() -> Response:
    content = request.get_json()
    sellers = [Seller.create_from_dto(data) for data in content]
    seller_controller.create_all(sellers)
    return make_response(seller_controller.create_all(sellers), HTTPStatus.CREATED)


@seller_bp.delete("/all")
def delete_all_sellers() -> Response:
    seller_controller.delete_all()
    return make_response("All Sellers deleted", HTTPStatus.OK)
