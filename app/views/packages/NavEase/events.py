class ScreenEventHandlers:

    def update_sections(self, event) -> None:
        # Actualizar las secciones del drawer
        index = event.control.selected_index
        print(index)
        # pass