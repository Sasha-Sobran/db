from mydb.auth.dao import car_dealership_addresses_dao
from mydb.auth.service.general_service import GeneralService


class CarDealershipAddressesService(GeneralService):
    _dao = car_dealership_addresses_dao
