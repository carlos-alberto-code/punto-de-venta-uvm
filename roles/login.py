import time
import flet as ft
from math import pi

class AnimatedBox(ft.Container):
        def __init__(self, border_color, bg_color, rotate_angle) -> None:
            super().__init__(
                width=48,
                height=48,
                border=ft.border.all(2.5, border_color),
                bgcolor=bg_color,
                border_radius=2,
                rotate=ft.transform.Rotate(rotate_angle, ft.alignment.center),
                animate_rotation=ft.animation.Animation(700, "easeInOut"),

            )


class Login(ft.Card):

    def __init__(self, page: ft.Page) -> None:
        super().__init__(
            width=400,
            height=612,
            elevation=15,
            content=ft.Container(
                bgcolor='#23262a',
                border_radius=6,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Divider(height=10, color='transparent'),
                        ft.Stack(
                            controls=[
                                AnimatedBox('#e9665a', None, 0),
                                AnimatedBox('#f7df6dd', '#23262a', pi / 4),
                            ]
                        )
                    ]
                )
            )
        )
        self.the_page = page
        self.page_configuration()
        self.animate_boxes()
    
    def page_configuration(self):
        self.the_page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.the_page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.the_page.bgcolor = '#1f262f'
    
    def animate_boxes(self):
        clock_wise_rotate = pi / 4
        counter_clock_wise_rotate = -pi * 2
        red_box = self.the_page.controls[0].content.content.controls[1].controls[0].controls[0]
        blue_box = self.the_page.controls[0].content.content.controls[1].controls[1].controls[0]
        counter = 0
        while True:
             if counter >= 0 and counter <= 4:
                red_box.rotate = ft.transform.Rotate(counter_clock_wise_rotate, ft.alignment.center)
                red_box.update()
                counter_clock_wise_rotate -= pi / 2
                counter += 1
                time.sleep(0.7)
