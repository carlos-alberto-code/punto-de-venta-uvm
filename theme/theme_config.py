from dataclasses import dataclass, field, asdict
import flet as ft


# TODO: Implementar Strategy para hacer permitir el cambio en tiempo de ejecución

@dataclass
class _LightColorPalette:
    #Paleta de colores
    #D95560 #2B3040 #8C8C8C #D94E4E #F2F2F2
    # Colores principales para tema claro
    primary:                str = field(default='#D9525E')  # bright red-orange
    on_primary:             str = field(default='#FFFFFF')  # blanco
    primary_container:      str = field(default='#BBDEFB')  # azul claro
    on_primary_container:   str = field(default='#0D47A1')  # azul oscuro
    secondary:              str = field(default='#03A9F4')  # cian
    on_secondary:           str = field(default='#FFFFFF')  # blanco
    secondary_container:    str = field(default='#D9525E')  # cian claro
    on_secondary_container: str = field(default='#181D26')  # cian oscuro
    tertiary:               str = field(default='#FFC107')  # ámbar
    on_tertiary:            str = field(default='#000000')  # negro
    tertiary_container:     str = field(default='#FFECB3')  # ámbar claro
    on_tertiary_container:  str = field(default='#FF6F00')  # ámbar oscuro
    error:                  str = field(default='#F44336')  # rojo
    on_error:               str = field(default='#FFFFFF')  # blanco
    error_container:        str = field(default='#FFCDD2')  # rojo claro
    on_error_container:     str = field(default='#B71C1C')  # rojo oscuro

    # Colores de fondo y superficie para tema claro
    background:             str = field(default='#FFFFFF')  # blanco
    on_background:          str = field(default='#000000')  # negro
    surface:                str = field(default='#FFFFFF')  # blanco
    on_surface:             str = field(default='#000000')  # negro
    surface_variant:        str = field(default='#F5F5F5')  # gris muy claro
    on_surface_variant:     str = field(default='#424242')  # gris oscuro

    # Color de bordes para tema claro
    outline:                str = field(default='#BDBDBD')  # gris medio
    outline_variant:        str = field(default='#E0E0E0')  # gris claro

    # Color de sombras para tema claro
    shadow:                 str = field(default='#000000')  # negro
    scrim:                  str = field(default='#000000')  # negro
    inverse_surface:        str = field(default='#303030')  # gris oscuro
    on_inverse_surface:     str = field(default='#FFFFFF')  # blanco
    inverse_primary:        str = field(default='#82B1FF')  # azul claro
    surface_tint:           str = field(default='#2196F3')  # azul"""

@dataclass
class _DarkColorPalette:
    
    # Paleta de colores
    #D9525E #282E40 #181D26 #D94E4E #F2F2F2
    # Dark Mode
    primary:                str = field(default='#D9525E')  # bright red-orange
    on_primary:             str = field(default='#181D26')  # darker gray-blue
    primary_container:      str = field(default='#181D26')  # darker gray-blue
    on_primary_container:   str = field(default='#D9525E')  # bright red-orange
    secondary:              str = field(default='#282E40')  # dark gray-blue
    on_secondary:           str = field(default='#181D26')  # darker gray-blue
    secondary_container:    str = field(default='#181D26')  # darker gray-blue
    on_secondary_container: str = field(default='#D9525E')  # bright red-orange
    tertiary:               str = field(default='#D94E4E')  # darker red-orange
    on_tertiary:            str = field(default='#181D26')  # darker gray-blue
    tertiary_container:     str = field(default='#181D26')  # darker gray-blue
    on_tertiary_container:  str = field(default='#D9525E')  # bright red-orange
    error:                  str = field(default='#D94E4E')  # darker red-orange
    on_error:               str = field(default='#181D26')  # darker gray-blue
    error_container:        str = field(default='#181D26')  # darker gray-blue
    on_error_container:     str = field(default='#D9525E')  # bright red-orange

    background:             str = field(default='#181D26')  # darker gray-blue
    on_background:          str = field(default='#FFFFFF')  # bright red-orange
    surface:                str = field(default='#181D26')  # darker gray-blue
    on_surface:             str = field(default='#FFFFFF')  # bright red-orange
    surface_variant:        str = field(default='#282E40')  # dark gray-blue
    on_surface_variant:     str = field(default='#F2F2F2')  # light gray

    outline:                str = field(default='#282E40')  # dark gray-blue
    outline_variant:        str = field(default='#F2F2F2')  # light gray

    shadow:                 str = field(default='#282E40')  # dark gray-blue
    scrim:                  str = field(default='#282E40')  # dark gray-blue
    inverse_surface:        str = field(default='#F2F2F2')  # light gray
    on_inverse_surface:     str = field(default='#181D26')  # darker gray-blue
    inverse_primary:        str = field(default='#D9525E')  # bright red-orange
    surface_tint:           str = field(default='#D9525E')  # bright red-orange"""
                                        
_light_color_palette = asdict(_LightColorPalette())
_dark_color_palette  = asdict(_DarkColorPalette())


_light_text_theme = ft.TextTheme(
    title_large=ft.TextStyle(size=21, font_family="Roboto", color=_LightColorPalette.on_background),
    body_medium=ft.TextStyle(size=14, font_family="Lato", color=_LightColorPalette.on_background),
)


_dark_text_theme = ft.TextTheme(
    title_large=ft.TextStyle(size=21, font_family="Roboto", color=_DarkColorPalette.on_background),
    body_medium=ft.TextStyle(size=14, font_family="Lato", color=_DarkColorPalette.on_background),
)


LightTheme = ft.Theme(
    color_scheme=ft.ColorScheme(**_light_color_palette),
    text_theme=_light_text_theme
)



DarkTheme = ft.Theme(
    color_scheme=ft.ColorScheme(**_dark_color_palette),
    text_theme=_dark_text_theme
)

