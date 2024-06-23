from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship 
from sqlalchemy import ForeignKey, Integer, String, DECIMAL, Date, CHAR, CheckConstraint


Base = declarative_base()


class Unit(Base):
    __tablename__ = 'units'
    
    id:   Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)


class Category(Base):
    __tablename__ = 'categories'

    id:   Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)


class Brand(Base):
    __tablename__ = 'brands'

    id:   Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)


class Product(Base):
    __tablename__ = 'products'
    __table_args__ = (
        CheckConstraint('quantity >= 0'),
        CheckConstraint('cost_price >= 0'),
        CheckConstraint('selling_price >= 0'),
        CheckConstraint('reorder_level >= 0'),
    )

    sku: Mapped[int]               = mapped_column(Integer, primary_key=True, autoincrement=True)
    unit_id: Mapped[int]           = mapped_column(Integer, ForeignKey('units.id'), nullable=False)
    category_id: Mapped[int]       = mapped_column(Integer, ForeignKey('categories.id'), nullable=False)
    brand_id: Mapped[int]          = mapped_column(Integer, ForeignKey('brands.id'), nullable=False)
    quantity: Mapped[int]          = mapped_column(Integer, nullable=False)
    cost_price: Mapped[DECIMAL]    = mapped_column(DECIMAL(10, 2), nullable=False)
    selling_price: Mapped[DECIMAL] = mapped_column(DECIMAL(10, 2), nullable=False)
    reorder_level:  Mapped[int]    = mapped_column(Integer, nullable=False, default=1)

    unit     = relationship("Unit", backref="products")
    brand    = relationship("Brand", backref="products")
    category = relationship("Category", backref="products")


class Supplier(Base):
    __tablename__ = 'suppliers'

    id:    Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name:  Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    address: Mapped[str] = mapped_column(String(50), nullable=False)
    phone: Mapped[str] = mapped_column(CHAR(10), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)


class Purchase(Base):
    __tablename__ = 'purchases'
    __table_args__ = (
        CheckConstraint('total >= 0'),
    )

    id:          Mapped[int]     = mapped_column(Integer, primary_key=True, autoincrement=True)
    supplier_id: Mapped[int]     = mapped_column(Integer, ForeignKey('suppliers.id'), nullable=False)
    date:        Mapped[Date]    = mapped_column(Date, nullable=False)
    total:       Mapped[DECIMAL] = mapped_column(DECIMAL(10, 2), nullable=False)

    supplier = relationship("Supplier", backref="purchases")


class PurchaseDetail(Base):
    __tablename__ = 'purchase_details'
    __table_args__ = (
        CheckConstraint('quantity > 0'),
        CheckConstraint('unit_purchase_price >= 0'),
        CheckConstraint('total_unit_price >= 0'),
    )

    purchase_id:         Mapped[int]     = mapped_column(Integer, ForeignKey('purchases.id'), primary_key=True, nullable=False)
    product_id:          Mapped[int]     = mapped_column(Integer, ForeignKey('products.sku'), primary_key=True, nullable=False)
    quantity:            Mapped[int]     = mapped_column(Integer, nullable=False)
    unit_purchase_price: Mapped[DECIMAL] = mapped_column(DECIMAL(10, 2), nullable=False)
    total_unit_price:    Mapped[DECIMAL] = mapped_column(DECIMAL(10, 2), nullable=False)

    purchase = relationship("Purchase", backref="purchase_details")
    product  = relationship("Product", backref="purchase_details")


class Customer(Base):
    __tablename__ = 'customers'
    __table_args__ = (
        CheckConstraint('age >= 18'),
    )

    id:        Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(50), nullable=False)
    age:       Mapped[int] = mapped_column(Integer, nullable=False)
    email:     Mapped[str] = mapped_column(String(50), nullable=False, unique=True)


class Sale(Base):
    __tablename__ = 'sales'
    __table_args__ = (
        CheckConstraint('total >= 0'),
    )

    id:          Mapped[int]     = mapped_column(Integer, primary_key=True, autoincrement=True)
    customer_id: Mapped[int]     = mapped_column(Integer, ForeignKey('customers.id'), nullable=False)
    date:        Mapped[Date]    = mapped_column(Date, nullable=False)
    total:       Mapped[DECIMAL] = mapped_column(DECIMAL(10, 2), nullable=False)

    customer = relationship("Customer", backref="sales")

class SaleDetail(Base):
    __tablename__ = 'sale_details'
    __table_args__ = (
        CheckConstraint('quantity > 0'),
        CheckConstraint('unit_sale_price >= 0'),
        CheckConstraint('total_unit_price >= 0'),
    )

    sale_id:          Mapped[int]     = mapped_column(Integer, ForeignKey('sales.id'), primary_key=True, nullable=False)
    product_id:       Mapped[int]     = mapped_column(Integer, ForeignKey('products.sku'), primary_key=True, nullable=False)
    quantity:         Mapped[int]     = mapped_column(Integer, nullable=False)
    unit_sale_price:  Mapped[DECIMAL] = mapped_column(DECIMAL(10, 2), nullable=False)
    total_unit_price: Mapped[DECIMAL] = mapped_column(DECIMAL(10, 2), nullable=False)

    sale    = relationship("Sale", backref="sale_details")
    product = relationship("Product", backref="sale_details")

# Modelos para la gestion de usuarios y roles

class ThemeMode(Base):
    __tablename__ = 'theme_modes'

    id:   Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)


class Role(Base):
    __tablename__ = 'roles'

    id:   Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)


class Modules(Base):
    __tablename__ = 'modules'

    id:   Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)


class User(Base):
    __tablename__ = 'users'
    __table_args__ = (
        CheckConstraint('age >= 18'),
    )

    id:            Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    full_name:     Mapped[str] = mapped_column(String(50), nullable=False)
    age:           Mapped[int] = mapped_column(Integer, nullable=False)
    whatsapp:      Mapped[str] = mapped_column(CHAR(10), nullable=False, unique=True)
    username:      Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    password:      Mapped[str] = mapped_column(String(50), nullable=False)
    role_id:       Mapped[int] = mapped_column(Integer, ForeignKey('roles.id'), nullable=False, default=0)
    theme_mode_id: Mapped[int] = mapped_column(Integer, ForeignKey('theme_modes.id'), nullable=False, default=0)

    role       = relationship("Role", backref="users")
    theme_mode = relationship("ThemeMode", backref="users")


class RoleModule(Base):
    __tablename__ = 'roles_modules'

    role_id:    Mapped[int] = mapped_column(Integer, ForeignKey('roles.id'), primary_key=True, nullable=False)
    module_id:  Mapped[int] = mapped_column(Integer, ForeignKey('modules.id'), primary_key=True, nullable=False)

    role   = relationship("Role", backref="roles_modules")
    module = relationship("Modules", backref="roles_modules")
