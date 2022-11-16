class Parqueadero:
    def __init__(self, hora: int, horario: str, num_espacios) -> None:
        self.hora = hora
        self.horario = horario
        self.num_espacios = num_espacios
    
    @property
    def asignar_espacios(self) -> None:
        pass