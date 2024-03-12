import flet as ft


_purchase = ft.NavigationDestination(
    icon=ft.icons.ARTICLE,
    label="Compras",
)

_sales = ft.NavigationDestination(
    icon=ft.icons.MONEY,
    label="Ventas",
)

_inventory = ft.NavigationDestination(
    icon=ft.icons.STORE_MALL_DIRECTORY,
    label="Inventario",
)

_customers = ft.NavigationDestination(
    icon=ft.icons.PEOPLE,
    label="Clientes",
)

_reports = ft.NavigationDestination(
    icon=ft.icons.DATA_SAVER_OFF,
    label="Reportes",
)

_point_of_sale = ft.NavigationDestination(
    icon=ft.icons.CABIN,
    label="Punto de Venta",
)


# Encapsulamientos de destinos por usuario

class UserPermissions:

    def __init__(self) -> None:
        self._permissions = {}

    @property
    def modules(self):
        return self._permissions
    
    def __getitem__(self, key):
        return self._permissions[key]

    # def __setitem__(self, key, value):
    #     self._permissions[key] = value
    
    def __iter__(self):
        return iter(self._permissions)
    
    def __len__(self):
        return len(self._permissions)

    def module_keys(self):
        return self._permissions.keys()


class AdminModules(UserPermissions):

    def __init__(self) -> None:
        super().__init__()
        self._permissions = {
            _purchase.label: _purchase,
            _inventory.label: _inventory,
            _sales.label: _sales,
            _customers.label: _customers,
            _reports.label: _reports,
        }


class EmployeeModules(UserPermissions):

    def __init__(self) -> None:
        super().__init__()
        self._permissions = {
            _inventory.label: _inventory,
            _sales.label: _sales,
            _customers.label: _customers,
            _point_of_sale.label: _point_of_sale,
        }
