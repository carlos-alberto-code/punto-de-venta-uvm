# Script para insertar 10 proveedores en la base de datos
from database.connection import get_db
from repository.controllers import SuplierController

# Una lista de 10 proveedores de una tienda de abarrotes en México
suppliers = [
    {
        "name": "La Costeña",
        "address": "Calle 1, Colonia 2, Ciudad 3, Estado 4",
        "phone": "1233567890",
        "email": "lacostena@example.com"
    },
    {
        "name": "Bimbo",
        "address": "Calle 5, Colonia 6, Ciudad 7, Estado 8",
        "phone": "0987854321",
        "email": "bimbo@example.com"
    },
    {
        "name": "Sabritas",
        "address": "Calle 9, Colonia 10, Ciudad 11, Estado 12",
        "phone": "9876543217",
        "email": "sabritas@example.com"
    },
    {
        "name": "Coca-Cola",
        "address": "Calle 13, Colonia 14, Ciudad 15, Estado 16",
        "phone": "0123456788",
        "email": "cocacola@example.com"
    },
    {
        "name": "Pepsi",
        "address": "Calle 17, Colonia 18, Ciudad 19, Estado 20",
        "phone": "9976543211",
        "email": "pepsi@example.com"
    },
    {
        "name": "Nestlé",
        "address": "Calle 21, Colonia 22, Ciudad 23, Estado 24",
        "phone": "0123456889",
        "email": "nestle@example.com"
    },
    {
        "name": "Kellogg's",
        "address": "Calle 25, Colonia 26, Ciudad 27, Estado 28",
        "phone": "9876543212",
        "email": "kelloggs@example.com"
    },
    {
        "name": "Lala",
        "address": "Calle 29, Colonia 30, Ciudad 31, Estado 32",
        "phone": "0123456789",
        "email": "lala@example.com"
    },
    {
        "name": "Gamesa",
        "address": "Calle 33, Colonia 34, Ciudad 35, Estado 36",
        "phone": "9876543210",
        "email": "gamesa@example.com"
    },
    {
        "name": "Barcel",
        "address": "Calle 37, Colonia 38, Ciudad 39, Estado 40",
        "phone": "0723456789",
        "email": "barcel@example.com"
    }
]

def insert_suppliers():
    controller = SuplierController()
    for supplier in suppliers:
        controller.insert(**supplier)
    print("10 suppliers inserted successfully")

if __name__ == "__main__":
    insert_suppliers()
