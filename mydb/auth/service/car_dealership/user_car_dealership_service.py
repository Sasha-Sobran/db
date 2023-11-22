from mydb.auth.dao import user_car_dealership_dao
from mydb.auth.service.general_service import GeneralService


class UserCarDealershipService(GeneralService):
    _dao = user_car_dealership_dao
