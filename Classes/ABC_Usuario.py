from abc import ABC, abstractmethod

class ABC_Usuario(ABC):
    """
    Clase abstracta para las clases de cada usuario
    """
    @property
    @abstractmethod
    def parquear_carro (self):
        """
        Metodo abstracto para parquear el carro
        """
        pass
    
    @property
    @abstractmethod
    def retirar_carro (self):
        """
        Metodo abstracta para retirar el carro
        """
        pass
