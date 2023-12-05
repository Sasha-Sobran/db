from mydb.auth.service.advertisement.advertisement_service import AdvertisementService
from mydb.auth.service.advertisement.comment_service import CommentService
from mydb.auth.service.advertisement.image_service import ImageService
from mydb.auth.service.car.car_service import CarService
from mydb.auth.service.car.car_type_service import CarTypeService
from mydb.auth.service.car.motor_service import MotorService
from mydb.auth.service.car.test_drive_service import TestDriveService
from mydb.auth.service.car_dealership.car_dealership_addresses_service import (
    CarDealershipAddressesService,
)
from mydb.auth.service.car_dealership.car_dealership_seller_service import (
    CarDealershipSellerService,
)
from mydb.auth.service.car_dealership.car_dealership_service import CarDealershipService
from mydb.auth.service.car_dealership.user_car_dealership_service import (
    UserCarDealershipService,
)
from mydb.auth.service.user.seller_service import SellerService
from mydb.auth.service.user.user_service import UserService

car_type_service = CarTypeService()
motor_service = MotorService()
car_service = CarService()
test_drive_service = TestDriveService()
car_dealership_service = CarDealershipService()
car_dealership_addresses_service = CarDealershipAddressesService()
user_service = UserService()
seller_service = SellerService()
user_car_dealership_service = UserCarDealershipService()
car_dealership_seller_service = CarDealershipSellerService()
advertisement_service = AdvertisementService()
image_service = ImageService()
comment_service = CommentService()
