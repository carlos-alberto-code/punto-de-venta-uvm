from typing                     import Optional
from business_objects.Customer  import Customer
from datetime                   import datetime
from business_objects.SaleDetail import SaleDetail


class Sale:
    
    def __init__(self, id: Optional[int], customer: Optional[Customer], datetime: datetime, total: float, sale_details: list[SaleDetail]) -> None:
        self._id = id
        self._customer = customer
        self._date = datetime.date()
        self._time = datetime.time()
        self._total = total
        self._sale_details = sale_details
    
    @property
    def id(self) -> Optional[int]:
        return self._id

    @property
    def customer(self) -> Optional[Customer]:
        return self._customer

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
    def details(self) -> list[SaleDetail]:
        return self._sale_details
    
    def __repr__(self) -> str:
        return f"Sale({self._id}, {self._customer}, {self._date}, {self._total})"