from database.connection import get_db
from controllers.controllers import UserController


def insert_users():
    with get_db() as db:
        user_controller = UserController()
        user_controller.insert(
            full_name='Carlos Alberto Baltazar Hinojosa',
            age=24,
            whatsapp='7151203279',
            username='carlos',
            password='cabh',
        )
        user_controller.insert(
            full_name='José Yael Montes López',
            age=22,
            whatsapp='7151313997',
            username='jose',
            password='yei',
        )
        user_controller.insert(
            full_name='Abigail Mercado Ramírez',
            age=30,
            whatsapp='1234567890',
            username='abi',
            password='abi123',
        )
        user_controller.insert(
            full_name='Abigail Mercado Ramírez',
            age=30,
            whatsapp='0987654321',
            username='abigail',
            password='abigail123',
        )

insert_users()
