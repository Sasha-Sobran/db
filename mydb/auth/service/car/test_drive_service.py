from mydb.auth.dao import test_drive_dao
from mydb.auth.service.general_service import GeneralService


class TestDriveService(GeneralService):
    _dao = test_drive_dao
