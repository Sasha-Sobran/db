from flask import Flask

from .car.car_route import car_bp
from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    app.register_blueprint(car_bp)
