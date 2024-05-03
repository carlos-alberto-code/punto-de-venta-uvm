import sys
sys.path.append('..')

from controllers.brands_controller import BrandsController


def view_brands(controller):
    for entity in controller.get_all_brands():
        print(entity.name)


controller = BrandsController()
for result in controller.search_brand('l'):
    print(result.name)  