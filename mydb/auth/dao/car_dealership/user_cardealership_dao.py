from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.car_dealership.user_cardealership import UserCarDealership


class UserCarDealershipDao(GeneralDAO):
    _domain_type = UserCarDealership
