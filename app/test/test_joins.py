import sys
sys.path.append('..')

from sqlalchemy import or_

from app.database.connection import get_db
from models.models import Product, Unit, Category, Brand


def search_products(db, search_string, limit=10):
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

with get_db() as db:
    search_string = 'Á'
    products = search_products(db, search_string)
    for product, unit, category, brand in products:
        print(f"{unit.name} {category.name} {brand.name}".upper())
