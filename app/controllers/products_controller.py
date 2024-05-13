from sqlalchemy import or_
from sqlalchemy.orm import joinedload

from database.connection import get_db
from database.models import Product, Category, Brand, Unit


class ProductController:
    """
    Este controlador se encarga de manejar las operaciones relacionadas con los productos.
    Puede hacer las siguientes operaciones:
    - Obtener todos los productos.
    - Obtener un producto por su ID.
    - Filtrar productos por categoría
    - Filtrar productos por marca
    - Filtrar productos por unidad
    - Buscar productos por una cadena de búsqueda (Aún no implementado)
    - Actualizar los datos de un producto.
    """

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
    
    def filter_by_category(self, category_id):
        return self._product_query().filter(Category.id == category_id).all()
    
    def filter_by_brand(self, brand_id):
        return self._product_query().filter(Brand.id == brand_id).all()
    
    def filter_by_unit(self, unit_id):
        return self._product_query().filter(Unit.id == unit_id).all()
    
    def update_product(self, product_id, **kwargs):
        with get_db() as db:
            product = db.query(Product).filter(Product.sku == product_id).first()
            for key, value in kwargs.items():
                setattr(product, key, value)
            db.commit()
            return product