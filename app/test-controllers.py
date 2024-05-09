import sys
sys.path.append('..')

from app.page.packages.forms import controller
from controllers.crud_repository import CrudRepository
from database.connection import get_db
from models.models import Unit


def view_all(controller):
    for entity in controller.get_all():
        print(entity.name)
    print()

