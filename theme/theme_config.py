from dataclasses import dataclass, field, asdict
import flet as ft


# TODO: Implementar Strategy para hacer permitir el cambio en tiempo de ejecución

@dataclass
class _LightColorPalette:
    #Paleta de colores basada en azul
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

    #Paleta de colores basada en morado
    """# Colores principales para tema claro
    primary:                str = field(default='#6200EA')  # Morado
    on_primary:             str = field(default='#FFFFFF')  # Blanco
    primary_container:      str = field(default='#EDE7F6')  # Morado Muy Claro
    on_primary_container:   str = field(default='#311B92')  # Morado Oscuro
    secondary:              str = field(default='#7C4DFF')  # Morado Brillante
    on_secondary:           str = field(default='#FFFFFF')  # Blanco
    secondary_container:    str = field(default='#D1C4E9')  # Morado Claro
    on_secondary_container: str = field(default='#512DA8')  # Morado Oscuro
    tertiary:               str = field(default='#FF4081')  # Rosa Brillante
    on_tertiary:            str = field(default='#000000')  # Negro
    tertiary_container:     str = field(default='#F8BBD0')  # Rosa Claro
    on_tertiary_container:  str = field(default='#C2185B')  # Rosa Oscuro
    error:                  str = field(default='#B00020')  # Rojo Oscuro
    on_error:               str = field(default='#FFFFFF')  # Blanco
    error_container:        str = field(default='#FFCDD2')  # Rojo Claro
    on_error_container:     str = field(default='#B71C1C')  # Rojo Oscuro

    # Colores de fondo y superficie para tema claro
    background:             str = field(default='#FFFFFF')  # Blanco
    on_background:          str = field(default='#000000')  # Negro
    surface:                str = field(default='#FFFFFF')  # Blanco
    on_surface:             str = field(default='#000000')  # Negro
    surface_variant:        str = field(default='#F5F5F5')  # Gris Muy Claro
    on_surface_variant:     str = field(default='#424242')  # Gris Oscuro

    # Color de bordes para tema claro
    outline:                str = field(default='#BDBDBD')  # Gris Medio
    outline_variant:        str = field(default='#E0E0E0')  # Gris Claro

    # Color de sombras para tema claro
    shadow:                 str = field(default='#000000')  # Negro
    scrim:                  str = field(default='#000000')  # Negro
    inverse_surface:        str = field(default='#303030')  # Gris Oscuro
    on_inverse_surface:     str = field(default='#FFFFFF')  # Blanco
    inverse_primary:        str = field(default='#B39DDB')  # Morado Suave
    surface_tint:           str = field(default='#6200EA')  # Morado"""

    #Monocromatica azul
    """# Colores principales para tema claro
    primary:                str = field(default='#1976D2')  # Azul
    on_primary:             str = field(default='#FFFFFF')  # Blanco
    primary_container:      str = field(default='#BBDEFB')  # Azul Claro
    on_primary_container:   str = field(default='#0D47A1')  # Azul Oscuro
    secondary:              str = field(default='#2196F3')  # Azul Brillante
    on_secondary:           str = field(default='#FFFFFF')  # Blanco
    secondary_container:    str = field(default='#90CAF9')  # Azul Suave
    on_secondary_container: str = field(default='#1565C0')  # Azul Medio
    tertiary:               str = field(default='#64B5F6')  # Azul Medio
    on_tertiary:            str = field(default='#FFFFFF')  # Blanco
    tertiary_container:     str = field(default='#E3F2FD')  # Azul Muy Claro
    on_tertiary_container:  str = field(default='#1E88E5')  # Azul Intenso
    error:                  str = field(default='#B00020')  # Rojo Oscuro
    on_error:               str = field(default='#FFFFFF')  # Blanco
    error_container:        str = field(default='#FFCDD2')  # Rojo Claro
    on_error_container:     str = field(default='#B71C1C')  # Rojo Oscuro

    # Colores de fondo y superficie para tema claro
    background:             str = field(default='#E3F2FD')  # Azul Muy Claro
    on_background:          str = field(default='#0D47A1')  # Azul Oscuro
    surface:                str = field(default='#FFFFFF')  # Blanco
    on_surface:             str = field(default='#0D47A1')  # Azul Oscuro
    surface_variant:        str = field(default='#BBDEFB')  # Azul Claro
    on_surface_variant:     str = field(default='#0D47A1')  # Azul Oscuro

    # Color de bordes para tema claro
    outline:                str = field(default='#90CAF9')  # Azul Suave
    outline_variant:        str = field(default='#BBDEFB')  # Azul Claro

    # Color de sombras para tema claro
    shadow:                 str = field(default='#000000')  # Negro
    scrim:                  str = field(default='#000000')  # Negro
    inverse_surface:        str = field(default='#303030')  # Gris Oscuro
    on_inverse_surface:     str = field(default='#FFFFFF')  # Blanco
    inverse_primary:        str = field(default='#BBDEFB')  # Azul Claro
    surface_tint:           str = field(default='#1976D2')  # Azul"""

    # Light Mode
    """primary:                str = field(default='#D95560')  # bright orange
    on_primary:             str = field(default='#F2F2F2')  # light gray
    primary_container:      str = field(default='#F2F2F2')  # light gray
    on_primary_container:   str = field(default='#2B3040')  # dark gray-blue
    secondary:              str = field(default='#2B3040')  # dark gray-blue
    on_secondary:           str = field(default='#F2F2F2')  # light gray
    secondary_container:    str = field(default='#F2F2F2')  # light gray
    on_secondary_container: str = field(default='#8C8C8C')  # medium gray
    tertiary:               str = field(default='#D94E4E')  # darker orange
    on_tertiary:            str = field(default='#F2F2F2')  # light gray
    tertiary_container:     str = field(default='#F2F2F2')  # light gray
    on_tertiary_container:  str = field(default='#2B3040')  # dark gray-blue
    error:                  str = field(default='#D94E4E')  # darker orange
    on_error:               str = field(default='#F2F2F2')  # light gray
    error_container:        str = field(default='#F2F2F2')  # light gray
    on_error_container:     str = field(default='#8C8C8C')  # medium gray

    background:             str = field(default='#F2F2F2')  # light gray
    on_background:          str = field(default='#2B3040')  # dark gray-blue
    surface:                str = field(default='#F2F2F2')  # light gray
    on_surface:             str = field(default='#2B3040')  # dark gray-blue
    surface_variant:        str = field(default='#8C8C8C')  # medium gray
    on_surface_variant:     str = field(default='#F2F2F2')  # light gray

    outline:                str = field(default='#2B3040')  # dark gray-blue
    outline_variant:        str = field(default='#8C8C8C')  # medium gray

    shadow:                 str = field(default='#2B3040')  # dark gray-blue
    scrim:                  str = field(default='#2B3040')  # dark gray-blue
    inverse_surface:        str = field(default='#8C8C8C')  # medium gray
    on_inverse_surface:     str = field(default='#F2F2F2')  # light gray
    inverse_primary:        str = field(default='#D95560')  # bright orange
    surface_tint:           str = field(default='#D95560')  # bright orange"""

@dataclass
class _DarkColorPalette:
    #Paleta de colores basada en azul
    """# Colores principales para tema oscuro
    primary:                str = field(default='#2196F3')  # azul
    on_primary:             str = field(default='#000000')  # negro
    primary_container:      str = field(default='#0D47A1')  # azul oscuro
    on_primary_container:   str = field(default='#BBDEFB')  # azul claro
    secondary:              str = field(default='#03A9F4')  # cian
    on_secondary:           str = field(default='#000000')  # negro
    secondary_container:    str = field(default='#01579B')  # cian oscuro
    on_secondary_container: str = field(default='#B3E5FC')  # cian claro
    tertiary:               str = field(default='#FFC107')  # ámbar
    on_tertiary:            str = field(default='#000000')  # negro
    tertiary_container:     str = field(default='#FF6F00')  # ámbar oscuro
    on_tertiary_container:  str = field(default='#FFECB3')  # ámbar claro
    error:                  str = field(default='#F44336')  # rojo
    on_error:               str = field(default='#000000')  # negro
    error_container:        str = field(default='#B71C1C')  # rojo oscuro
    on_error_container:     str = field(default='#FFCDD2')  # rojo claro

    # Colores de fondo y superficie para tema oscuro
    background:             str = field(default='#121212')  # negro puro
    on_background:          str = field(default='#FFFFFF')  # blanco
    surface:                str = field(default='#121212')  # negro puro
    on_surface:             str = field(default='#FFFFFF')  # blanco
    surface_variant:        str = field(default='#424242')  # gris oscuro
    on_surface_variant:     str = field(default='#F5F5F5')  # gris muy claro

    # Color de bordes para tema oscuro
    outline:                str = field(default='#757575')  # gris medio
    outline_variant:        str = field(default='#BDBDBD')  # gris claro

    # Color de sombras para tema oscuro
    shadow:                 str = field(default='#000000')  # negro
    scrim:                  str = field(default='#000000')  # negro
    inverse_surface:        str = field(default='#FFFFFF')  # blanco
    on_inverse_surface:     str = field(default='#303030')  # gris oscuro
    inverse_primary:        str = field(default='#BBDEFB')  # azul claro
    surface_tint:           str = field(default='#2196F3')  # azul"""

    #Paleta de colores basada en morado
    """# Colores principales para tema oscuro
    primary:                str = field(default='#BB86FC')  # Morado Claro
    on_primary:             str = field(default='#000000')  # Negro
    primary_container:      str = field(default='#3700B3')  # Morado Oscuro
    on_primary_container:   str = field(default='#EDE7F6')  # Morado Muy Claro
    secondary:              str = field(default='#7C4DFF')  # Morado Brillante
    on_secondary:           str = field(default='#000000')  # Negro
    secondary_container:    str = field(default='#512DA8')  # Morado Oscuro
    on_secondary_container: str = field(default='#D1C4E9')  # Morado Claro
    tertiary:               str = field(default='#FF4081')  # Rosa Brillante
    on_tertiary:            str = field(default='#000000')  # Negro
    tertiary_container:     str = field(default='#C2185B')  # Rosa Oscuro
    on_tertiary_container:  str = field(default='#F8BBD0')  # Rosa Claro
    error:                  str = field(default='#CF6679')  # Rojo Claro
    on_error:               str = field(default='#000000')  # Negro
    error_container:        str = field(default='#B71C1C')  # Rojo Oscuro
    on_error_container:     str = field(default='#FFCDD2')  # Rojo Claro

    # Colores de fondo y superficie para tema oscuro
    background:             str = field(default='#121212')  # Negro Puro
    on_background:          str = field(default='#FFFFFF')  # Blanco
    surface:                str = field(default='#121212')  # Negro Puro
    on_surface:             str = field(default='#FFFFFF')  # Blanco
    surface_variant:        str = field(default='#424242')  # Gris Oscuro
    on_surface_variant:     str = field(default='#F5F5F5')  # Gris Muy Claro

    # Color de bordes para tema oscuro
    outline:                str = field(default='#757575')  # Gris Medio
    outline_variant:        str = field(default='#BDBDBD')  # Gris Claro

    # Color de sombras para tema oscuro
    shadow:                 str = field(default='#000000')  # Negro
    scrim:                  str = field(default='#000000')  # Negro
    inverse_surface:        str = field(default='#FFFFFF')  # Blanco
    on_inverse_surface:     str = field(default='#303030')  # Gris Oscuro
    inverse_primary:        str = field(default='#6200EA')  # Morado
    surface_tint:           str = field(default='#BB86FC')  # Morado Claro"""

    #Monocromatica azul
    """# Colores principales para tema oscuro
    primary:                str = field(default='#90CAF9')  # Azul Claro
    on_primary:             str = field(default='#000000')  # Negro
    primary_container:      str = field(default='#1565C0')  # Azul Medio
    on_primary_container:   str = field(default='#E3F2FD')  # Azul Muy Claro
    secondary:              str = field(default='#64B5F6')  # Azul Medio
    on_secondary:           str = field(default='#000000')  # Negro
    secondary_container:    str = field(default='#1E88E5')  # Azul Intenso
    on_secondary_container: str = field(default='#E3F2FD')  # Azul Muy Claro
    tertiary:               str = field(default='#2196F3')  # Azul Brillante
    on_tertiary:            str = field(default='#000000')  # Negro
    tertiary_container:     str = field(default='#1976D2')  # Azul
    on_tertiary_container:  str = field(default='#E3F2FD')  # Azul Muy Claro
    error:                  str = field(default='#CF6679')  # Rojo Claro
    on_error:               str = field(default='#000000')  # Negro
    error_container:        str = field(default='#B71C1C')  # Rojo Oscuro
    on_error_container:     str = field(default='#FFCDD2')  # Rojo Claro

    # Colores de fondo y superficie para tema oscuro
    background:             str = field(default='#121212')  # Negro Puro
    on_background:          str = field(default='#E3F2FD')  # Azul Muy Claro
    surface:                str = field(default='#121212')  # Negro Puro
    on_surface:             str = field(default='#E3F2FD')  # Azul Muy Claro
    surface_variant:        str = field(default='#424242')  # Gris Oscuro
    on_surface_variant:     str = field(default='#90CAF9')  # Azul Claro

    # Color de bordes para tema oscuro
    outline:                str = field(default='#757575')  # Gris Medio
    outline_variant:        str = field(default='#BDBDBD')  # Gris Claro

    # Color de sombras para tema oscuro
    shadow:                 str = field(default='#000000')  # Negro
    scrim:                  str = field(default='#000000')  # Negro
    inverse_surface:        str = field(default='#FFFFFF')  # Blanco
    on_inverse_surface:     str = field(default='#303030')  # Gris Oscuro
    inverse_primary:        str = field(default='#1976D2')  # Azul
    surface_tint:           str = field(default='#90CAF9')  # Azul Claro"""

    # Colores principales
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

