from sqlalchemy import desc as desc_order

from database.connection import get_db
from database.models import Product, Category, Brand, Unit


class ProductController:
    # TODO: Agregar paginación cuando sean muchos productos.
    # TODO: Agregar validación de datos.
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
                Product.cost_price,
                Product.selling_price,
                Product.reorder_level,
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
    
    def get_all(self, order_by=None):
        return self._product_query().order_by(order_by).all()
    
    def get_by_id(self, product_id):
        return self._product_query().filter(Product.sku == product_id).first()

    def filter_by(self, model, id, order_by=None, desc=False):
        query = self._product_query().filter(model.id == id)
        if desc and order_by:
            query = query.order_by(desc_order(order_by))
        elif order_by:
            query = query.order_by(order_by)
        return query.all()
    
    def update_product(self, product_id, **kwargs):
        with get_db() as db:
            product = db.query(Product).filter(Product.sku == product_id).first()
            for key, value in kwargs.items():
                setattr(product, key, value)
            db.commit()
            return product
    