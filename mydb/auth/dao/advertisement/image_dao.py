from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.advertisement.image import Image


class ImageDao(GeneralDAO):
    _domain_type = Image
