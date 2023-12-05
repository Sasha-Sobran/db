from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.car.test_drive import TestDrive


class TestDriveDao(GeneralDAO):
    _domain_type = TestDrive
