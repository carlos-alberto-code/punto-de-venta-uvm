import random
from database.connection import get_db
from database.models import Product, Unit, Category, Brand


# Comprobar si las tablas Unit, Category y Brand tienen registros para que este script pueda funcionar
def exist_data():
    with get_db() as db:
        units = db.query(Unit).all()
        categories = db.query(Category).all()
        brands = db.query(Brand).all()
        if not units or not categories or not brands:
            return False
        return True

# Una función para obtener todos las unidades
def get_units():
    with get_db() as db:
        units = db.query(Unit).all()
        return units

# Una función para obtener todos las categorías
def get_categories():
    with get_db() as db:
        categories = db.query(Category).all()
        return categories

# Una función para obtener todos las marcas
def get_brands():
    with get_db() as db:
        brands = db.query(Brand).all()
        return brands
    
# Obtener los ids de las unidades, categorías y marcas
units_ids = [unit.id for unit in get_units()]
categories_ids = [category.id for category in get_categories()]
brands_ids = [brand.id for brand in get_brands()]

# Si existen registros en las tablas Unit, Category y Brand, entonces insertar 100 productos
if exist_data():
    with get_db() as db:
        if not db.query(Product).first():
            # Crear e insertar 100 productos
            for i in range(100):
                producto = Product(
                    # Una unidad aleatoria
                    unit_id=random.choice(units_ids),
                    # Una categoría aleatoria
                    category_id=random.choice(categories_ids),
                    # Una marca aleatoria
                    brand_id=random.choice(brands_ids),
                    # Cantidad aleatoria entre 1 y 30
                    quantity=random.randint(1, 30),
                    # Precio de compra aleatorio entre 1 y 100
                    cost_price=random.randint(1, 100),
                    # Precio de venta aleatorio entre 1 y 100
                    selling_price=random.randint(1, 100),
                    # Stock mínimo aleatorio entre 1 y 10
                    reorder_level=random.randint(1, 10),
                    # Descripción aleatoria
                )
                db.add(producto)
            db.commit()
            print('Productos insertados exitosamente')
        else:
            existing_products = db.query(Product).count()
            if existing_products < 100:
                # Insertar productos adicionales hasta llegar a 100
                for i in range(existing_products + 1, 101):
                    producto = Product(
                        id=i,
                        # Una unidad aleatoria
                        unit_id=random.choice(units_ids),
                        # Una categoría aleatoria
                        category_id=random.choice(categories_ids),
                        # Una marca aleatoria
                        brand_id=random.choice(brands_ids),
                        # Cantidad aleatoria entre 1 y 30
                        quantity=random.randint(1, 30),
                        # Precio de compra aleatorio entre 1 y 100
                        cost_price=random.randint(1, 100),
                        # Precio de venta aleatorio entre 1 y 100
                        selling_price=random.randint(1, 100),
                        # Stock mínimo aleatorio entre 1 y 10
                        reorder_level=random.randint(1, 10),
                        # Descripción aleatoria
                    )
                    db.add(producto)
                db.commit()
                print('Productos insertados exitosamente')
            else:
                print('Ya existen 100 productos en la base de datos')