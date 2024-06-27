from business_objects.Sale import Sale
from business_objects.Customer import Customer
from business_objects.SaleDetails import SaleDetails
from business_objects.product_properties import Product

from repository.repository import Repository


class SalesManager:

    def __init__(self) -> None:
        self.customer = Customer()
        self.product = Product()
        self.sale = Sale()
        self.sale_detail = SaleDetails()
    
    def save_sale(self) -> None:
        pass