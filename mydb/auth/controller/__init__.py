from mydb.auth.controller.advertisement.comment_controller import CommentController
from mydb.auth.controller.advertisement.advertisement_controller import AdvertisementController
from mydb.auth.controller.advertisement.image_controller import ImageController
from mydb.auth.controller.car.car_controller import CarController
from mydb.auth.controller.car.car_type_controller import CarTypeController
from mydb.auth.controller.car.motor_controller import MotorController
from mydb.auth.controller.car.test_drive_controller import TestDriveController
from mydb.auth.controller.car_dealership.car_dealership_seller_controller import CarDealershipSellerController
from mydb.auth.controller.car_dealership.car_dealership_controller import CarDealershipController
from mydb.auth.controller.car_dealership.user_car_dealership_controller import UserCarDealershipController
from mydb.auth.controller.user.seller_controller import SellerController
from mydb.auth.controller.user.user_controller import UserController

car_type_controller = CarTypeController()
motor_controller = MotorController()
car_controller = CarController()
test_drive_controller = TestDriveController()
car_dealership_controller = CarDealershipController()
user_controller = UserController()
seller_controller = SellerController()
user_car_dealership_controller = UserCarDealershipController()
car_dealership_seller_controller = CarDealershipSellerController()
advertisement_controller = AdvertisementController()
image_controller = ImageController()
comment_controller = CommentController()
