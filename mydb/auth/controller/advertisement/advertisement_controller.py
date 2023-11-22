from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import advertisement_service


class AdvertisementController(GeneralController):
    _service = advertisement_service
