from fpdf import FPDF

class Ticket(FPDF):
    def __init__(self, negocio: str, fecha: str, hora: str, productos: list[tuple], total: int):
        super().__init__(orientation='P', unit='mm', format='A5')
        self.negocio = negocio
        self.fecha = fecha
        self.hora = hora
        self.productos = productos
        self.total = total
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
        total = self.total
        self.cell(0, 10, f"Total: ${total:,.2f} MXN", 0, 0, "R")

    def generar_ticket(self):
        self.add_page()
        self.set_font("Arial", "B", 10)
        # Ajustar los anchos de las celdas para acomodar la nueva columna
        self.cell(20, 10, "Cantidad", ln=False, align="C")
        self.cell(50, 10, "Producto", ln=False, align="L")
        self.cell(30, 10, "Precio de venta", ln=False, align="L")
        self.cell(30, 10, "Total", ln=True, align="R")
        self.set_font("Arial", "", 8)
        
        for cantidad, descripcion, precio_venta, precio_total in self.productos:
            self.cell(20, 7, str(cantidad), ln=False, align="C")
            self.cell(50, 7, descripcion, ln=False, align="L")
            self.cell(30, 7, f"${precio_venta:.2f}", ln=False, align="L")
            self.cell(30, 7, f"${precio_total:.2f}", ln=True, align="R")
        
        self.output("ticket.pdf", "F")

# Ejemplo de uso
productos = [
    # (cantidad(int), descripcion(str), precio_de_venta(float), precio_total(float))
    (3, "Coca-Cola 355 ML", 10, 30),
    (2, "Bolsa Arroz Morelos", 42, 84),
    (7, "Mostaza MacCormic", 2, 14)
]

ticket = Ticket("Mi Negocio", "2022-01-01", "12:00 PM", productos, 128)
ticket.generar_ticket()
