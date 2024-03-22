import flet as ft


class DrawerControls:
    def __init__(self) -> None:
        self.top_controls = [] # Controles fijos
        self.middle_controls = [] # Controles dinámicos
        self.bottom_controls = [] # Controles fijos

def main(page: ft.Page):
    
    from view.modules.modules_declaration import create_modules
    modules = create_modules() # Se cran los módulos como lista de objetos Module


    drawer = ft.NavigationDrawer()

    def funcion_de_cambio(event):
        index = event.control.selected_index
        module = modules[index] # Obtenemos el módulo en el índice donde se cambio
        sections = module.sections # Obtenemos las secciones del módulo
        sections = [section.build() for section in sections] # Construimos las secciones
        drawer_controls = DrawerControls()
        drawer_controls.middle_controls = sections
        drawer.controls = [
            *drawer_controls.top_controls,
            *drawer_controls.middle_controls,
            *drawer_controls.bottom_controls
        ]
        drawer.open = True
        page.update()

    navbar = ft.NavigationBar(
        destinations=[module.rail.build() for module in modules],
        on_change=funcion_de_cambio
    )

    page.drawer = ft.NavigationDrawer(

    )

    page.appbar = ft.AppBar(
        title=ft.Text('Aplicación'),
    )
    page.navigation_bar = navbar
    page.update()

    

ft.app(target=main)
