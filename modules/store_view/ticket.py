from fpdf import FPDF

class Ticket(FPDF):
    def __init__(self, negocio: str, fecha: str, hora: str, productos: list[tuple]):
        super().__init__(orientation='P', unit='mm', format='A5')
        self.negocio = negocio
        self.fecha = fecha
        self.hora = hora
        self.productos = productos

    def header(self):
        self.set_font("Arial", "B", 18)
        self.cell(0, 10, self.negocio, ln=True, align="C")
        self.set_font("Arial", "", 10)
        self.cell(0, 10, f"Fecha: {self.fecha}", ln=True, align="C")
        self.cell(0, 10, f"Hora: {self.hora}", ln=True, align="C")
        self.ln(10)

    def footer(self):
        total = sum(cantidad * precio for cantidad, _, precio in self.productos)
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Total: ${total:,.2f} MXN", 0, 0, "R")

    def generar_ticket(self):
        self.add_page()
        self.set_font("Arial", "B", 12)
        # lineas de separación
        self.cell(0, 10, "-"*90, ln=True)
        self.cell(30, 10, "Cantidad", ln=False, align="L")
        self.cell(90, 10, "Producto", ln=False, align="L")
        self.cell(30, 10, "Total", ln=True, align="L")
        self.set_font("Arial", "", 10)
        for cantidad, producto, precio in self.productos:
            self.cell(30, 10, str(cantidad), ln=False, align="L")
            self.cell(90, 10, producto, ln=False, align="L")
            self.cell(30, 10, f"${precio * cantidad:.2f}", ln=True, align="L")

        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        total = sum(cantidad * precio for cantidad, _, precio in self.productos)
        self.cell(0, 10, f"Total: ${total:,.2f} MXN", 0, 0, "R")

        self.output("ticket.pdf", "F")

# Ejemplo de uso
productos = [
    (3, "Coca-Cola 355 ML", 100),
    (2, "Bolsa Arroz Morelos", 200),
    (7, "Mostaza MacCormic", 300)
]

ticket = Ticket("Mi Negocio", "2022-01-01", "12:00 PM", productos)
ticket.generar_ticket()