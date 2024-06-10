import flet as ft


class FormProductCard(ft.ListTile):

    def __init__(self):
        super().__init__(
            leading=ft.Image()
        )


ft.Card()
class PurchaseForm(ft.Card):

    def __init__(self):
        super().__init__(
            width=350,
            height=600,
            elevation=10,
        )
        self._product_cards: list[ft.Card] = []
    
    def add_product_card(self, product_card: ft.Card):
        self._product_cards.append(product_card)
        # self.content = self._create_content()
        self.update()
    
    def _create_card(self):
        return FormProductCard()
    