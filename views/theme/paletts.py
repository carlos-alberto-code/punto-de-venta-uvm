from dataclasses import dataclass, field, asdict


@dataclass
class LightColorPalette:
    # Colores principales para tema claro
    primary:        str = field(default='#2A2B47')  # azul oscuro
    on_primary:     str = field(default='#F2F2F2')  # blanco grisáceo
    secondary:      str = field(default='#BFA8FF')  # lila
    on_secondary:   str = field(default='#2A2B47')  # azul oscuro
    tertiary:       str = field(default='#FEE6C2')  # melocotón claro
    on_tertiary:    str = field(default='#2A2B47')  # azul oscuro
    # Colores de fondo y superficie para tema claro
    background:     str = field(default='#DFDFDF')  # gris
    on_background:  str = field(default='#2A2B47')  # azul oscuro
    surface:        str = field(default='#F2F2F2')  # blanco grisáceo
    on_surface:     str = field(default='#2A2B47')  # azul oscuro
    # Color de bordes para tema claro
    outline:        str = field(default='#2A2B47')  # azul oscuro
    outline_variant:str = field(default='#BFA8FF')  # lila
    # Color de sombras para tema claro
    shadow:         str = field(default='#DFDFDF')  # gris
    scrim:          str = field(default='#DFDFDF')  # gris
    surface_tint:   str = field(default='#BFA8FF')  # lila


@dataclass
class DarkColorPalette:
    # Colores principales para tema oscuro
    primary:        str = field(default='#F2F2F2')  # blanco grisáceo
    on_primary:     str = field(default='#2A2B47')  # azul oscuro
    secondary:      str = field(default='#7F5AFF')  # lila oscuro
    on_secondary:   str = field(default='#F2F2F2')  # blanco grisáceo
    tertiary:       str = field(default='#B3845A')  # melocotón oscuro
    on_tertiary:    str = field(default='#F2F2F2')  # blanco grisáceo
    # Colores de fondo y superficie para tema oscuro
    background:     str = field(default='#2A2B47')  # azul oscuro
    on_background:  str = field(default='#DFDFDF')  # gris
    surface:        str = field(default='#2A2B47')  # azul oscuro
    on_surface:     str = field(default='#DFDFDF')  # gris
    # Color de bordes para tema oscuro
    outline:        str = field(default='#F2F2F2')  # blanco grisáceo
    outline_variant:str = field(default='#7F5AFF')  # lila oscuro
    # Color de sombras para tema oscuro
    shadow:         str = field(default='#2A2B47')  # azul oscuro
    scrim:          str = field(default='#2A2B47')  # azul oscuro
    surface_tint:   str = field(default='#7F5AFF')  # lila oscuro


# Paletas de colores en diccionario
_light_color_palette = asdict(LightColorPalette())
_dark_color_palette  = asdict(DarkColorPalette())
