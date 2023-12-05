from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import car_dealership_addresses_service


class CarDealershipAddressesController(GeneralController):
    _service = car_dealership_addresses_service
