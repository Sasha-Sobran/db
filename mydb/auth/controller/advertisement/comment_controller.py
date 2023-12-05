from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import comment_service


class CommentController(GeneralController):
    _service = comment_service
