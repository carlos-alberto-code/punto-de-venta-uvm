import sys
sys.path.append('..')

import unittest
from database.connection import get_db
from models.models import Unit
from controllers.crud_repository import CrudRepository

class TestCrudRepository(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with get_db() as database:
            cls.db = database
            cls.unit_repository = CrudRepository(Unit, cls.db)

    def tearDown(self) -> None:
        with get_db() as database:
            database.query(Unit).delete()
            database.commit()

    def test_get_all_units(self):
        units = self.unit_repository.get_all()
        self.assertIsInstance(units, list)

    def test_validate_name(self):
        with self.assertRaises(ValueError):
            self.unit_repository.create('')  # Intenta crear una instancia con un nombre vacío
        with self.assertRaises(ValueError):
            self.unit_repository.create('!@#')  # Intenta crear una instancia con un nombre que contiene caracteres no alfanuméricos
        with self.assertRaises(ValueError):
            self.unit_repository.create('ab')  # Intenta crear una instancia con un nombre que tiene menos de 3 caracteres
        with self.assertRaises(ValueError):
            self.unit_repository.create('a'*21)  # Intenta crear una instancia con un nombre que tiene más de 20 caracteres

    def test_create_unit_with_valid_name(self):
        self.unit_repository.create('Unidad de prueba')
        units = self.unit_repository.get_all()
        self.assertEqual(len(units), 1)
    

if __name__ == '__main__':
    unittest.main()