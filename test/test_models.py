import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.models import Base, Unit, Brand, Category, Product


class TestModels(unittest.TestCase):

    def setUp(self) -> None:
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    
    def test_create_unit(self):
        new_unit = Unit(name='Unidad de prueba')
        self.session.add(new_unit)
        self.session.commit()

        unit = self.session.query(Unit).first()
        self.assertIsNotNone(unit)
        self.assertEqual(unit.name, 'Unidad de prueba') # type: ignore
    
    def test_create_brand(self):
        new_brand = Brand(name='Quaker')
        self.session.add(new_brand)
        self.session.commit()

        brand = self.session.query(Brand).first()
        self.assertIsNotNone(brand)
        self.assertEqual(brand.name, 'Quaker') # type: ignore
    
    def test_create_category(self):
        new_category = Category(name='Cereales')
        self.session.add(new_category)
        self.session.commit()

        category = self.session.query(Category).first()
        self.assertIsNotNone(category)
        self.assertEqual(category.name, 'Cereales') # type: ignore
    
    def test_create_product(self):
        new_product = Product(
            unit_id=1,
            brand_id=1,
            category_id=1,
            quantity=10,
            purchase_price=10.0,
            sale_price=15.0,
            minimum_stock=5,
            description='Avena Quaker'
        )
        self.session.add(new_product)
        self.session.commit()

        product = self.session.query(Product).first()
        self.assertIsNotNone(product)
        self.assertEqual(product.description, 'Avena Quaker') # type: ignore

    def tearDown(self) -> None:
        self.session.close()
        Base.metadata.drop_all(self.engine)


if __name__ == '__main__':
    unittest.main()

