import sqlalchemy

from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.car.car_type import CarType


class CarTypeDao(GeneralDAO):
    _domain_type = CarType

    def create(self, obj: object) -> object:
        """
        Creates object in database table.
        :param obj: object to create in Database
        :return: created object
        """
        self._session.execute(sqlalchemy.text("CALL insert_into_car_type(:name)"), {"name": obj.name})
        self._session.commit()
        return obj

    def create_rows(self):
        self._session.execute(sqlalchemy.text("CALL insert_rows_in_package()"))
        self._session.commit()
