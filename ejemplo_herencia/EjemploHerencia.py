# Crear un docente con nombramiento
docente1 = DocenteNombramiento(1, "Juan", "Pérez", 1500)
docente1.agregar_horas_extra(10)

# Crear un docente que trabaja por factura
docente2 = DocenteFactura(2, "Ana", "Gómez", 2000)

# Mostrar información de los docentes
print(docente1)
print(docente2)

class Docente:
    def __init__(self, id_docente, nombre, apellido):
        self.id_docente = id_docente
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"Docente: {self.nombre} {self.apellido} (ID: {self.id_docente})"
class DocenteNombramiento(Docente):
    def __init__(self, id_docente, nombre, apellido, salario_base):
        super().__init__(id_docente, nombre, apellido)
        self.salario_base = salario_base
        self.horas_extra = 0
        self.valor_hora_extra = 10  # Valor fijo por hora extra, puede ser cambiado

    def agregar_horas_extra(self, horas):
        self.horas_extra += horas

    def calcular_sueldo_mensual(self):
        return self.salario_base + (self.horas_extra * self.valor_hora_extra)

    def __str__(self):
        sueldo = self.calcular_sueldo_mensual()
        return f"{super().__str__()} - Salario Base: ${self.salario_base}, Horas Extra: {self.horas_extra}, Sueldo Mensual: ${sueldo}"
class DocenteFactura(Docente):
    def __init__(self, id_docente, nombre, apellido, valor_factura):
        super().__init__(id_docente, nombre, apellido)
        self.valor_factura = valor_factura
        self.iva = 0.12  # IVA del 12%

    def calcular_valor_final(self):
        valor_iva = self.valor_factura * self.iva
        valor_final = self.valor_factura - valor_iva
        return valor_final, valor_iva

    def __str__(self):
        valor_final, valor_iva = self.calcular_valor_final()
        return f"{super().__str__()} - Valor Factura: ${self.valor_factura}, Valor IVA: ${valor_iva}, Valor Final: ${valor_final}"
