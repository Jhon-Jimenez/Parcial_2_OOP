
class Vehiculo:
    def __init__(self, tipo: str, dias: int, horas: int, minutos: int, pago: float) -> None:
        self.tipo = tipo
        self.dias = dias
        self.horas = horas
        self.minutos = minutos
        self.pago = pago
    
    @property
    def __str__(self):
        return "El vehiculo de tipo " + self.tipo + " duró " + str(self.dias) + " días con "  + str(self.horas) + " horas y "  + str(self.minutos) + " minutos en el parqueadero"
    
    @property
    def calcular_pago(self) -> None:
        valor_minutos = 0
        valor_horas = 0
        valor_dias = 0
        if self.tipo == "compact":
            valor_minutos = 5
            valor_horas = 10
            valor_dias = 20
        elif self.tipo == "suv":
            valor_minutos = 10
            valor_horas = 20
            valor_dias = 40
        elif self.tipo == "van":
            valor_minutos = 20
            valor_horas = 40
            valor_dias = 80
        else:
            raise ValueError("Solo se aceptan tres tipos de vehiculos")

        print("Calculando el valor a pagar...")    
        tiempo = self.dias * valor_dias + self.horas * valor_horas + self.minutos * valor_minutos
        self.pago = tiempo
    
    @property
    def get_pago(self) -> float:
        self.calcular_pago()
        return self.pago