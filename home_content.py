import flet as ft


class HomeContent(ft.Container):
    def __init__(self, user: str):
        super().__init__(
            col=10.80,
            padding=15,
            content=ft.Column(
                [
                    ft.Lottie(
                        src='https://raw.githubusercontent.com/xvrh/lottie-flutter/master/example/assets/Mobilo/A.json',
                        repeat=False,
                        reverse=False,
                        animate=True,
                    ),
                    ft.Text(value=f'Bienvenido a la App {user.title()}', size=30),
                    ft.Rive(
                        'rive/w_solana_hero.riv',
                        placeholder=ft.ProgressBar(),
                        # width=300,
                        # height=200,
                        expand=True,
                        # scale=1.3,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            
        )
