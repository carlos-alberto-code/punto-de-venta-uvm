import flet as ft

# from page.login import LoginPage
from controllers.role_controller import RoleController
from page.user_view import UserView, OwnerView, EmployeeView

from controllers.unit_controller import UnitControllerTest


def main(page: ft.Page):

    page.theme_mode = ft.ThemeMode.LIGHT  # Se remplaza por las preferencias de usuario

    # roles_controller = RoleController()
    # roles_controller.delete_role(1)

    unt = UnitControllerTest()
    unt.new_unit(name='Metro')

ft.app(target=main)
