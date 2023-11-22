from mydb.auth.dao import comment_dao
from mydb.auth.service.general_service import GeneralService


class CommentService(GeneralService):
    _dao = comment_dao
