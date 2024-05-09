import sys
sys.path.append('..')

from controllers.crud_repository import CrudRepository
from database.connection import get_db
from models.models import Unit


def view_all(controller):
    for entity in controller.get_all():
        print(entity.name)

# with get_db() as db:
#     controller = CrudRepository(model=Unit, session=db)
#     view_all(controller)

with get_db() as db:
    controller = CrudRepository(model=Unit, session=db)
    controller.create('bolsa')
    view_all(controller)
 