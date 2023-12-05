import sqlalchemy

from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.car_dealership.user_cardealership import UserCarDealership


class UserCarDealershipDao(GeneralDAO):
    _domain_type = UserCarDealership

    def insert_user_car_dealership(self, user_name: str, car_dealership_name: str):
        self._session.execute(sqlalchemy.text("CALL insert_into_junction_table(:car_dealership_name, :user_name)"),
                              {"car_dealership_name": car_dealership_name, "user_name": user_name})
        self._session.commit()
