from sqlalchemy import or_

from database.connection import get_db
from models.models import Product, Category, Brand, Unit


class ProductController:
    
    @staticmethod
    def search_products(search_string, limit=10):
        with get_db() as db:
            return db.query(Product, Unit, Category, Brand)\
                .join(Unit, Product.unit_id == Unit.id)\
                .join(Category, Product.category_id == Category.id)\
                .join(Brand, Product.brand_id == Brand.id)\
                .filter(or_(
                    Product.description.ilike(f'%{search_string}%'),
                    Unit.name.ilike(f'%{search_string}%'),
                    Category.name.ilike(f'%{search_string}%'),
                    Brand.name.ilike(f'%{search_string}%')
                ))\
                .limit(limit)\
                .all()
    
    @staticmethod
    def get_all():
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
            .join(Brand, Product.brand_id == Brand.id)\
            .all()