from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import test_drive_service


class TestDriveController(GeneralController):
    _service = test_drive_service
