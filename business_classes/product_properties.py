class Category:
    def __init__(self, category_id: int, name: str):
        self.category_id = category_id
        self.name = name
    
    def __repr__(self):
        return f'Category(name={self.name})'
    
    
class Brand:
    def __init__(self, brand_id: int, name: str):
        self.brand_id = brand_id
        self.name = name

    def __repr__(self):
        return f'Brand(name={self.name})'

class Unit:
    def __init__(self, unit_id: int, name: str):
        self.unit_id = unit_id
        self.name = name

    def __repr__(self):
        return f'Unit(name={self.name})'