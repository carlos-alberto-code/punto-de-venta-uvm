from fpdf import FPDF

class Ticket(FPDF):
    def __init__(self, negocio: str, fecha: str, hora: str, productos: list[tuple]):
        super().__init__(orientation='P', unit='mm', format='A5')
        self.negocio = negocio
        self.fecha = fecha
        self.hora = hora
        self.productos = productos
        self.set_margins(10, 10, 10)  # Ajustar márgenes

    def header(self):
        self.set_font("Arial", "B", 18)
        self.cell(0, 10, self.negocio, ln=True, align="C")
        self.set_font("Arial", "", 10)
        self.cell(0, 10, f"Fecha: {self.fecha}", ln=True, align="C")
        self.cell(0, 10, f"Hora: {self.hora}", ln=True, align="C")
        self.ln(5)
        self.cell(0, 0, "", "B", 1, 'C')  # Línea de separación después del encabezado
        self.ln(5)  # Espacio después de la línea de separación

    def footer(self):
        self.set_y(-20)  # Posiciona el pie de página 20 mm antes del final de la página
        self.cell(0, 0, "", "T", 1, 'C')  # Línea de separación antes del pie de página
        self.set_font("Arial", "I", 10)
        total = sum(cantidad * precio for cantidad, _, precio in self.productos)
        self.cell(0, 10, f"Total: ${total:,.2f} MXN", 0, 0, "R")

    def generar_ticket(self):
        self.add_page()
        self.set_font("Arial", "B", 12)
        # lineas de separación
        self.cell(30, 10, "Cantidad", ln=False, align="C")
        self.cell(70, 10, "Producto", ln=False, align="L")
        self.cell(40, 10, "Total", ln=True, align="C")
        self.set_font("Arial", "", 10)
        
        espacio_disponible = self.h - self.b_margin - self.get_y()  # Altura disponible en la página
        altura_producto = 10  # Altura que ocupa cada producto en la lista
        
        for cantidad, producto, precio in self.productos:
            if espacio_disponible >= altura_producto:
                self.cell(30, 10, str(cantidad), ln=False, align="C")
                self.cell(70, 10, producto, ln=False, align="L")  # Se ajusta el ancho aquí también
                self.cell(40, 10, f"${precio * cantidad:.2f}", ln=True, align="C")  # Y aquí
                espacio_disponible -= altura_producto
            else:
                # Si no hay suficiente espacio, se podría agregar una nueva página o ajustar el diseño.
                # Por simplicidad, aquí detenemos la adición de más productos.
                break
    
        self.output("ticket.pdf", "F")

# Ejemplo de uso
productos = [
    (3, "Coca-Cola 355 ML", 100),
    (2, "Bolsa Arroz Morelos", 200),
    (7, "Mostaza MacCormic", 300)
]

ticket = Ticket("Mi Negocio", "2022-01-01", "12:00 PM", productos)
ticket.generar_ticket()