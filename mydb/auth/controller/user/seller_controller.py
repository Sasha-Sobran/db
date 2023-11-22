from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import seller_service


class SellerController(GeneralController):
    _service = seller_service

    def get_advertisements(self, id: int):
        return [advertisement.put_into_dto() for advertisement in self._service.get_advertisements(id)]
