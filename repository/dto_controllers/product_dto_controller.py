from business_classes.Product import Product
from repository.controllers  import ProductController
from interface.ControllerInterface import ControllerInterface as Controller


class ProductDTOController(Controller):
    
    def __init__(self) -> None:
        self.product_controller = ProductController()
    
    def get_all(self)-> list[Product]:
        all_products = self.product_controller.get_all()
        return [
            Product(
                product_id=product.sku,
                unit_name=product.unit,
                category_name=product.category,
                brand_name=product.brand,
                cost_price=product.cost_price,
                selling_price=product.selling_price,
                quantity=product.quantity,
                reorder_level=product.reorder_level,
            ) for product in all_products
        ]
    
    def get_by_id(self, id: int) -> Product | None:
        product = self.product_controller.get_by_id(id)
        if product:
            return Product(
                product_id=product.sku,
                unit_name=product.unit,
                category_name=product.category,
                brand_name=product.brand,
                cost_price=product.cost_price,
                selling_price=product.selling_price,
                quantity=product.quantity,
                reorder_level=product.reorder_level,
            )
    
    def insert(self, **data) -> None:
        self.product_controller.insert(**data)
    
    def update(self, id: int, **data) -> None:
        self.product_controller.update(id, **data)

    def search(self, search_term: str) -> list[Product] | None:
        results = self.product_controller.search(search_term)
        return [
            Product(
                product_id=product.sku,
                unit_name=product.unit,
                category_name=product.category,
                brand_name=product.brand,
                cost_price=product.cost_price,
                selling_price=product.selling_price,
                quantity=product.quantity,
                reorder_level=product.reorder_level,
            ) for product in results
        ]