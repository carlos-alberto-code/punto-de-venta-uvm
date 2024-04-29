import sys
sys.path.append('..')
from database.connection import get_db
from models.models import Product, Unit, Category, Brand

def get_products_with_details(db):
    return db.query(Product, Unit, Category, Brand).join(Unit, Product.unit_id == Unit.id).join(Category, Product.category_id == Category.id).join(Brand, Product.brand_id == Brand.id).all()

with get_db() as db:
    products = get_products_with_details(db)
    for index, (product, unit, category, brand) in enumerate(products, start=1):
        print(f"#{index} - {unit.name} {category.name} {brand.name}")


