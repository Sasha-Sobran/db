from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.car_dealership.car_dealership_addresses import (
    CarDealershipAddresses,
)


class CarDealershipAddressesDao(GeneralDAO):
    _domain_type = CarDealershipAddresses
