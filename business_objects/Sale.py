from typing                     import Optional
from business_objects.Customer  import Customer
from datetime                   import datetime as Date


class Sale:
    
    def __init__(self, id: Optional[int], customer: Optional[Customer], date: Date, total: float):
        self.id = id
        self.customer = customer
        self.date = date
        self.total = total
    
    def __repr__(self) -> str:
        return f"Sale({self.id}, {self.customer}, {self.date}, {self.total})"