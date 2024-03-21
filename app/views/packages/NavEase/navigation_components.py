'''
```>[!Nota] Una nota sobre el manejo de eventos de cambio

Para que las funciones que apoyan el evento de cambio ``on_change`` de los controles de navegación 
pueden surtir efecto en las clases que hemos creado heredando de ``ft.UserControl``, que es una plantilla
para crear nuevos componentes, es necesario que los eventos de cambio actúen cuando el componente se construye,
es decir, cuando se llama al método ``build`` y no en los atributos del componente.
```
'''

from .module import Module

from abc import ABC, abstractmethod
from typing import List
import flet as ft


class Appbar(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()
        self._theme_mode_control = ft.IconButton(icon=ft.icons.LIGHT_MODE)
        self._close_control = ft.IconButton(icon=ft.icons.CLOSE, on_click=lambda _: page.window_close())
    
    def build(self):
        # El hecho de que tengamos variables de instancia y las pasemos al Appbar, a la hora de los eventos
        # no significa que se actualicen. Actualizar los controles en función de los eventos parece
        # requerir acceder a las propiedades despues de implementar el método build.
        # En el caso del Appbar, no es necesario, pero en otros casos, como el Drawer, sí.
        return ft.AppBar(
            actions=[
                self._theme_mode_control,
                self._close_control,
            ]
        )


# Observador
class Observer(ABC):
    """
    Clase abstracta que sirve como interfaz para los observadores.
    Los observadores son los componentes que se actualizan cuando el sujeto cambia.
    En nuestro caso el sujeto es el Navbar y el observador es el componente Drawer.
    """
    @abstractmethod
    def update(self, sections: List[ft.NavigationDrawerDestination]):
        """Cada observador implementa este método, pero cada uno implementa su propia lógica"""
        pass


class Drawer(Observer, ft.UserControl):
    """
    Es un observador que se actualiza cuando el Navbar cambia.
    Es un contenedor que muestra las secciones de los módulos. En su papel de observador 
    actualiza las secciones ``ft.NavigationDrawerDestination`` cuando el Navbar cambia.
    """
    def __init__(self):
        super().__init__()
        self._drawer = ft.NavigationDrawer(open=True)

    def _build_menu_controls(self, specific_sections: List[ft.NavigationDrawerDestination] = []):
        menu_controls: List[ft.Control] = [
            ft.Container(height=14),
            ft.NavigationDrawerDestination(
                label='Usuario', # TODO: Debe cambiar y usar el nombre del usuario
                icon=ft.icons.PERSON, # TODO: Posiblemente la foto del usuario
            ),
            ft.Divider(),
            *specific_sections, # Agrega específicamente aquí las secciones intermedias
            ft.Divider(),
            ft.NavigationDrawerDestination(
                label='Configuración',
                icon=ft.icons.SETTINGS,
            ),
            ft.NavigationDrawerDestination(
                label='Cerrar sesión',
                icon=ft.icons.LOGOUT,
            ),
        ]
        return menu_controls
    
    # Método del observador para actualizar las secciones en el Drawer
    def update(self, sections: List[ft.NavigationDrawerDestination]):
        menu_controls = [
            ft.Container(height=14),
            ft.NavigationDrawerDestination(
                label='Usuario', # TODO: Debe cambiar y usar el nombre del usuario
                icon=ft.icons.PERSON, # TODO: Posiblemente la foto del usuario
            ),
            ft.Divider(),
            *sections, # Agrega específicamente aquí las secciones intermedias
            ft.Divider(),
            ft.NavigationDrawerDestination(label='Configuración', icon=ft.icons.SETTINGS),
            ft.NavigationDrawerDestination(label='Cerrar sesión', icon=ft.icons.LOGOUT),
        ]
        self._drawer.controls = menu_controls
        self._drawer.open = True
        self._drawer.update()


    def build(self):
        return self._drawer


class Navbar(ft.UserControl):
    """
    Navbar es un componente de navegación que permite al usuario cambiar entre diferentes módulos de la aplicación.
    Cuando se selecciona un módulo, Navbar notifica a todos los observadores registrados para que puedan actualizar su estado en consecuencia.
    """
    def __init__(self, modules: List[Module]):
        super().__init__()
        self._observers: List[Observer] = []
        self.modules = modules
        self._initial_index = 0
        initial_sections = self.modules[self._initial_index].sections
        self._notify([section.build() for section in initial_sections])

    def register(self, observer: 'Observer'):
        """
        Registra un nuevo observador. Cuando se selecciona un módulo, todos los observadores registrados serán notificados.
        """
        self._observers.append(observer)

    def unregister(self, observer: 'Observer'):
        """
        Elimina un observador. El observador ya no será notificado cuando se selecciona un módulo.
        """
        self._observers.remove(observer)

    def _notify(self, sections: List[ft.NavigationDrawerDestination]):
        """
        Notifica a todos los observadores registrados que se ha seleccionado un módulo, proporcionándoles las secciones del módulo seleccionado.
        """
        for observer in self._observers:
            observer.update(sections)

    def update_sections(self, event):
        """
        Maneja el evento de cambio de módulo seleccionado. Obtiene el índice del módulo seleccionado y notifica a los observadores.
        """
        index = event.control.selected_index
        sections = self.modules[index].sections
        sections = [section.build() for section in sections]
        self._notify(sections)

    def build(self):
        """
        Construye el componente de interfaz de usuario para el Navbar.
        """
        return ft.NavigationBar(
            selected_index=self._initial_index,
            destinations=[module.rail.build() for module in self.modules],
            on_change=self.update_sections
        )
