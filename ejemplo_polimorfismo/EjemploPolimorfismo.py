persona = Persona("Juan Pérez")

# Realizar algunos pagos
pago_agua = PagoAguaPotable(50.75)
pago_luz = PagoLuzElectrica(120.30)
pago_predial = PagoPredial(300.00)
pago_telefono = PagoTelefonoConvencional(45.20)

# Recibir pagos en la billetera de la persona
persona.billetera.recibir_pago(pago_agua)
persona.billetera.recibir_pago(pago_luz)
persona.billetera.recibir_pago(pago_predial)
persona.billetera.recibir_pago(pago_telefono)

# Mostrar todos los pagos realizados
persona.billetera.mostrar_pagos()


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.billetera = Billetera()

    def __str__(self):
        return f"Persona: {self.nombre}"
class Billetera:
    def __init__(self):
        self.pagos = []

    def recibir_pago(self, pago):
        self.pagos.append(pago)

    def mostrar_pagos(self):
        for pago in self.pagos:
            print(pago)
from abc import ABC, abstractmethod

class Pago(ABC):
    @abstractmethod
    def __str__(self):
        pass
class PagoAguaPotable(Pago):
    def __init__(self, monto):
        self.monto = monto

    def __str__(self):
        return f"Pago de Agua Potable: ${self.monto}"

class PagoLuzElectrica(Pago):
    def __init__(self, monto):
        self.monto = monto

    def __str__(self):
        return f"Pago de Luz Eléctrica: ${self.monto}"

class PagoPredial(Pago):
    def __init__(self, monto):
        self.monto = monto

    def __str__(self):
        return f"Pago Predial: ${self.monto}"

class PagoTelefonoConvencional(Pago):
    def __init__(self, monto):
        self.monto = monto

    def __str__(self):
        return f"Pago de Teléfono Convencional: ${self.monto}"
