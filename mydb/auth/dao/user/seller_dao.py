from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.user.seller import Seller


class SellerDao(GeneralDAO):
    _domain_type = Seller
