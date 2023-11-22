from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .car.car_type_route import car_type_bp
    from .car.motor_route import motor_bp
    from .car.car_route import car_bp
    from .car.test_drive_route import test_drive_bp
    from .advertisement.advertisement_route import advertisement_bp
    from .advertisement.image_route import image_bp
    from .advertisement.comment_route import comment_bp
    from .car_dealership.car_dealership_route import car_dealership_bp
    from .car_dealership.car_dealership_seller_route import car_dealership_seller_bp
    from .car_dealership.user_car_dealership_route import user_car_dealership_bp
    from .user.user_route import user_bp
    from .user.seller_route import seller_bp

    app.register_blueprint(car_type_bp)
    app.register_blueprint(motor_bp)
    app.register_blueprint(car_bp)
    app.register_blueprint(test_drive_bp)
    app.register_blueprint(advertisement_bp)
    app.register_blueprint(image_bp)
    app.register_blueprint(comment_bp)
    app.register_blueprint(car_dealership_bp)
    app.register_blueprint(car_dealership_seller_bp)
    app.register_blueprint(user_car_dealership_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(seller_bp)
