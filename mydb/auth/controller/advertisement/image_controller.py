from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import image_service


class ImageController(GeneralController):
    _service = image_service
