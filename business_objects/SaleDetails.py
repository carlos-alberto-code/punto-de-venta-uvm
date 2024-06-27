from business_objects.Sale      import Sale
from business_objects.Product   import Product


class SaleDetails:
    def __init__(
            self,
            sale:               Sale,
            product:            Product,
            quantity:           int,
            unit_sale_price:    float,
            total_unit_price:   float
    ) -> None:
        self.sale: Sale         = sale
        self.product: Product   = product
        self.quantity           = quantity
        self.unit_sale_price    = unit_sale_price
        self.total_unit_price   = total_unit_price
        self.total_price        = quantity * unit_sale_price
    
    def __repr__(self) -> str:
        return f"SaleDetails({self.sale}, {self.product}, {self.quantity}, {self.unit_sale_price}, {self.total_unit_price})"