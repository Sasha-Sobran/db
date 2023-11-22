from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.advertisement.advertisement import Advertisement


class AdvertisementDao(GeneralDAO):
    _domain_type = Advertisement
