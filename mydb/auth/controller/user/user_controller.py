from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import user_service


class UserController(GeneralController):
    _service = user_service

    def get_comments(self, id: int):
        return [self._service.get_comments(id)]
