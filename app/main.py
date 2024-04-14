import flet as ft

# from page.login import LoginPage
from controllers.role_controller import RoleTest
from page.user_view import UserView, OwnerView, EmployeeView


def main(page: ft.Page):

    page.theme_mode = ft.ThemeMode.LIGHT  # Se remplaza por las preferencias de usuario

    # page.add(LoginPage(page).build())
    roles = RoleTest()
    print(roles.get_role(3))

    user_view = UserView(OwnerView())
    user_view.build_view()
    user_view.view_strategy = EmployeeView()
    user_view.build_view()


ft.app(target=main)
