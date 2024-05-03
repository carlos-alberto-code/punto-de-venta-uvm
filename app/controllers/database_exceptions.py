class DataException(Exception):
    def __init__(self, tablename: str):
        super().__init__(f'There is no data in the table "{tablename}".')

class UnitAlreadyExists(Exception):
    def __init__(self, unit_name: str):
        super().__init__(f'The unit "{unit_name.lower()}" already exists in the table "units".')

class UnitNotFoundException(Exception):
    def __init__(self, unit_name: str):
        super().__init__(f'The unit "{unit_name.lower()}" does not exist in the table "units".')
