import sys
sys.path.append('..')
import unittest
from unittest.mock import patch, Mock
from controllers.units_controller import UnitsController


class TestUnitsController(unittest.TestCase):
    def setUp(self) -> None:
        self.controller = UnitsController()
    
    @patch('controllers.units_controller.get_db')
    def test_get_all_units(self, mock_get_db):
        mock_db = Mock()
        mock_get_db.return_value = mock_db
        mock_db.query().order_by().all.return_value = ['unit1', 'unit2', 'unit3']
        result = self.controller.get_all_units()
        self.assertEqual(self.controller.get_all_units(), ['unit1', 'unit2', 'unit3'])
    
    @patch('controllers.units_controller.get_db')
    def test_create_unit(self, mock_get_db):
        with patch('controllers.units_controller.get_db') as mock_get_db:
            mock_db = Mock()
            mock_get_db.return_value = mock_db
            self.controller.create_unit('unit1')
            mock_db.add.assert_called_once()
            mock_db.commit.assert_called_once()
    
    @patch('controllers.units_controller.get_db')
    def test_delete_unit(self, mock_get_db):
        with patch('controllers.units_controller.get_db') as mock_get_db:
            mock_db = Mock()
            mock_get_db.return_value = mock_db
            self.controller.delete_unit('unit1')
            mock_db.query().filter_by().first.assert_called_once()
            mock_db.delete.assert_called_once()
            mock_db.commit.assert_called_once()
    
    @patch('controllers.units_controller.get_db')
    def test_update_unit(self, mock_get_db):
        with patch('controllers.units_controller.get_db') as mock_get_db:
            mock_db = Mock()
            mock_get_db.return_value = mock_db
            self.controller.update_unit('unit1', 'unit2')
            mock_db.query().filter_by().first.assert_called_once()
            mock_db.commit.assert_called_once()


if __name__ == '__main__':
    unittest.main()