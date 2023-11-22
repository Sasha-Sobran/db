from mydb.auth.dao import motor_dao
from mydb.auth.service.general_service import GeneralService


class MotorService(GeneralService):
    _dao = motor_dao
