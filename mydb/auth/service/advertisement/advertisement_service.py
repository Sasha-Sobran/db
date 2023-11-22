from mydb.auth.dao import advertisement_dao
from mydb.auth.service.general_service import GeneralService


class AdvertisementService(GeneralService):
    _dao = advertisement_dao
