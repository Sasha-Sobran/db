from mydb.auth.dao import image_dao
from mydb.auth.service.general_service import GeneralService


class ImageService(GeneralService):
    _dao = image_dao
