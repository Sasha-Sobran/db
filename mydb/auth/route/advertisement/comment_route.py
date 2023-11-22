from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import comment_controller
from mydb.auth.domain.advertisement.comment import Comment

comment_bp = Blueprint("comments", __name__, url_prefix="/comments/")


@comment_bp.get("")
def get_all_comments() -> Response:
    return make_response(jsonify(comment_controller.find_all()), HTTPStatus.OK)


@comment_bp.get('/<int:comment_id>')
def get_comments(comment_id: int) -> Response:
    return make_response(jsonify(comment_controller.find_by_id(comment_id)), HTTPStatus.OK)


@comment_bp.put('/<int:comment_id>')
def update_comment(comment_id: int) -> Response:
    content = request.get_json()
    comment = Comment.create_from_dto(content)
    comment_controller.update(comment_id, comment)
    return make_response("Comment updated", HTTPStatus.OK)


@comment_bp.patch('/<int:comment_id>')
def patch_comment(comment_id: int) -> Response:
    content = request.get_json()
    comment_controller.patch(comment_id, content)
    return make_response("Comment updated", HTTPStatus.OK)


@comment_bp.delete('/<int:comment_id>')
def delete_comment(comment_id: int) -> Response:
    comment_controller.delete(comment_id)
    return make_response("Comment deleted", HTTPStatus.OK)


@comment_bp.post("")
def create_comment() -> Response:
    content = request.get_json()
    comment = Comment.create_from_dto(content)
    comment_id = comment_controller.create(comment)
    return make_response(f"Comment created with ID: {comment_id}", HTTPStatus.CREATED)


@comment_bp.post("/bulk")
def create_all_comments() -> Response:
    content = request.get_json()
    comments = [Comment.create_from_dto(data) for data in content]
    comment_controller.create_all(comments)
    return make_response(comment_controller.create_all(comments), HTTPStatus.CREATED)


@comment_bp.delete("/all")
def delete_all_comments() -> Response:
    comment_controller.delete_all()
    return make_response("All Comments deleted", HTTPStatus.OK)
