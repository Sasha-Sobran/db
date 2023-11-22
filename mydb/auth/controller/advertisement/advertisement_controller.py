from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import advertisement_service


class AdvertisementController(GeneralController):
    _service = advertisement_service

    def get_comments(self, id: int):
        return [self._service.get_comments(id)]

    def get_images(self, id):
        return [image.put_into_dto() for image in self._service.get_images(id)]
