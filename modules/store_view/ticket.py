import os
import tempfile
import webbrowser

from fpdf import FPDF
import os
import tempfile
import webbrowser
from fpdf import FPDF


class Ticket(FPDF):
    def __init__(self, business_name: str, date: str, hour: str, products: list[tuple], total: float):
        """
        Inicializa una instancia de la clase Ticket.

        Args:
            negocio (str): El nombre del negocio.
            fecha (str): La fecha del ticket.
            hora (str): La hora del ticket.
            productos (list[tuple]): Una lista de tuplas que representan los productos del ticket.
                Cada tupla debe contener cuatro valores: cantidad, descripción del producto,
                precio de venta unitario y total (cantidad multiplicado por el precio de venta unitario).
            total (int): El total del ticket.

        Returns:
            None
        """
        super().__init__(orientation='P', unit='mm', format='A5')
        self.negocio = business_name
        self.fecha = date
        self.hora = hour
        self.productos = products
        self.total = total
        self.set_margins(10, 10, 10)

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
        self.set_y(-40)  # Posiciona el pie de página 20 mm antes del final de la página
        self.cell(0, 0, "", "T", 1, 'C')  # Línea de separación antes del pie de página
        self.set_font("Arial", "I", 10)
        total = self.total
        iva = self.calculate_iva()
        subtotal = float(total) - iva
        self.cell(0, 10, f"Subtotal: ${subtotal:,.2f} MXN", 0, 1, "R")  # Asegurarse de que el subtotal se muestre correctamente
        self.cell(0, 10, f"IVA: ${iva:,.2f} MXN", 0, 1, "R")  # Mostrar el IVA
        self.cell(0, 10, f"Total: ${total:,.2f} MXN", 0, 1, "R")  # Mostrar el total

    def build_ticket(self):
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
    
    def show_in_browser(self):
        # Guardar el PDF en un archivo temporal
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmpfile:
            self.output(tmpfile.name, 'F')
            # Abrir el archivo temporal en el navegador
            webbrowser.open('file://' + os.path.realpath(tmpfile.name))

    def calculate_iva(self) -> float:
        return float(self.total) * 0.16
    