from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.advertisement.comment import Comment


class CommentDao(GeneralDAO):
    _domain_type = Comment
