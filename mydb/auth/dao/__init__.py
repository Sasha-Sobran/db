from .advertisement.advertisement_dao import AdvertisementDao
from .advertisement.comment_dao import CommentDao
from .advertisement.image_dao import ImageDao
from .car.car_dao import CarDao
from .car.car_type_dao import CarTypeDao
from .car.motor_dao import MotorDao
from .car.test_drive_dao import TestDriveDao
from .car_dealership.car_dealership_addresses_dao import CarDealershipAddressesDao
from .car_dealership.car_dealership_dao import CarDealershipDao
from .car_dealership.car_dealership_seller_dao import CarDealershipSellerDao
from .car_dealership.user_cardealership_dao import UserCarDealershipDao
from .user.seller_dao import SellerDao
from .user.user_dao import UserDao

car_type_dao = CarTypeDao()
motor_dao = MotorDao()
car_dao = CarDao()
test_drive_dao = TestDriveDao()
car_dealership_dao = CarDealershipDao()
user_dao = UserDao()
seller_dao = SellerDao()
user_car_dealership_dao = UserCarDealershipDao()
car_dealership_seller_dao = CarDealershipSellerDao()
car_dealership_addresses_dao = CarDealershipAddressesDao()
advertisement_dao = AdvertisementDao()
image_dao = ImageDao()
comment_dao = CommentDao()
