class PurchaseDetail:

    def __init__(self, purchase_id: int, product_id: int, quantity: int, unit_purchase_price: float, total_unit_price: float):
        self.purchase_id = purchase_id
        self.product_id = product_id
        self.quantity = quantity
        self.unit_purchase_price = unit_purchase_price
        self.total_unit_price = total_unit_price
    
    def __repr__(self) -> str:
        return (
            f'PurchaseDetail(purchase_id={self.purchase_id}, product_id={self.product_id}, '
            f'quantity={self.quantity}, unit_purchase_price={self.unit_purchase_price}, '
            f'total_unit_price={self.total_unit_price})'
        )