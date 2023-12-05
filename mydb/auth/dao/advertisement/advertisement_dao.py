import sqlalchemy

from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.advertisement.advertisement import Advertisement


class AdvertisementDao(GeneralDAO):
    _domain_type = Advertisement

    def get_avg_price(self, operation):
        result = self._session.execute(
            sqlalchemy.text("CALL mydb.get_avg(:p);"), {"p": operation}).fetchall()

        self._session.commit()
        return {"result": result[0][0]}
