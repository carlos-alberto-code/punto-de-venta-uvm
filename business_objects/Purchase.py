from typing import Optional, List
from business_objects.Supplier import Supplier
from datetime import datetime
from business_objects.PurchaseDetail import PurchaseDetail

class Purchase:
    def __init__(self, id: Optional[int], supplier: Optional[Supplier], datetime: datetime, total: float, purchase_details: List[PurchaseDetail]) -> None:
        self._id = id
        self._supplier = supplier
        self._date = datetime.date()
        self._time = datetime.time()
        self._total = total
        self._purchase_details = purchase_details

    @property
    def id(self) -> Optional[int]:
        return self._id

    @property
    def supplier(self) -> Optional[Supplier]:
        return self._supplier

    @property
    def date(self):
        return self._date

    @property
    def time(self):
        return self._time

    @property
    def total(self) -> float:
        return self._total

    @property
    def details(self) -> List[PurchaseDetail]:
        return self._purchase_details

    def __repr__(self) -> str:
        return f"Purchase({self._id}, {self._supplier}, {self._date}, {self._total})"