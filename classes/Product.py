class Product:
    def __init__(self, id, unit):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} costs {self.price} euros"

    def __repr__(self):
        return f"Product({self.name}, {self.price})"