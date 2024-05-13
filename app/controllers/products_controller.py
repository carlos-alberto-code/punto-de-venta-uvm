from sqlalchemy import or_
from sqlalchemy.orm import joinedload

from database.connection import get_db
from database.models import Product, Category, Brand, Unit


class ProductController:

    def _product_query(self):
        with get_db() as db:
            return db.query(
                Product.sku,
                Product.quantity,
                Product.purchase_price,
                Product.sale_price,
                Product.minimum_stock,
                Product.description,
                Unit.name.label('unit'),
                Category.name.label('category'),
                Brand.name.label('brand')
            ).join(Unit, Product.unit_id == Unit.id)\
            .join(Category, Product.category_id == Category.id)\
            .join(Brand, Product.brand_id == Brand.id)
    
    # def search_products(self, search_string, limit=10):
    #     with get_db() as db:
    #         return db.query(Product, Unit, Category, Brand)\
    #             .join(Unit, Product.unit_id == Unit.id)\
    #             .join(Category, Product.category_id == Category.id)\
    #             .join(Brand, Product.brand_id == Brand.id)\
    #             .filter(or_(
    #                 Product.description.ilike(f'%{search_string}%'),
    #                 Unit.name.ilike(f'%{search_string}%'),
    #                 Category.name.ilike(f'%{search_string}%'),
    #                 Brand.name.ilike(f'%{search_string}%')
    #             ))\
    #             .limit(limit)\
    #             .all()
    
    def get_all_products(self):
        return self._product_query().all()
    
    def get_by_id(self, product_id):
        return self._product_query().filter(Product.sku == product_id).first()