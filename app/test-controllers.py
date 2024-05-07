import sys
sys.path.append('..')

from app.controllers.crud_repository import CrudRepository
from database.connection import get_db
from models.models import Brand, Category, Unit


def view_brands(controller):
    for entity in controller.get_all():
        print(entity.name)

with get_db() as db:
    controller = CrudRepository(model=Unit, session=db)
    view_brands(controller)
 