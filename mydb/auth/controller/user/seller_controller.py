from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import seller_service


class SellerController(GeneralController):
    _service = seller_service
