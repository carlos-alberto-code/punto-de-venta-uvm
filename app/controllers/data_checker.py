from typing import Any

from database.connection import get_db
from models.models import Base


class DataChecker:

    def exist_data_in(self, model: Any) -> bool:
        with get_db() as db:
            return db.query(model).first() is not None
