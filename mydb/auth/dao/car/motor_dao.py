from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.car.motor import Motor


class MotorDao(GeneralDAO):
    _domain_type = Motor
