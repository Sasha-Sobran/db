from mydb.auth.dao import seller_dao
from mydb.auth.service.general_service import GeneralService


class SellerService(GeneralService):
    _dao = seller_dao
