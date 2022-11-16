from abc import ABC, abstractmethod

class ABC_Usuario(ABC):
    @property
    @abstractmethod
    def parquear_carro (self):
        pass
    
    @property
    @abstractmethod
    def retirar_carro (self):
        pass
