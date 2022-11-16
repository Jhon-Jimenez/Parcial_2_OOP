from ABC_Usuario import ABC_Usuario

class Usuario(ABC_Usuario):
    def __init__(self, nombre: str, cc: int) -> None:
        self.nombre = nombre
        self.cc = cc

    def parquear_carro(self, nombre: str, tipo: str, dias: int, horas: int, minutos: int) -> None:
        pass

    def retirar_carro(self, nombre: str, tipo: str, dias: int, horas: int, minutos: int) -> None:
        pass