#Las clases pueden ser abstractas
from abc import ABC, abstractmethod

class Inmueble(ABC):
    def __init__(self, direccion, codigo_postal, descripcion):
        self.direccion = direccion
        self.codigo_postal = codigo_postal
        self.descripcion = descripcion
    
    @abstractmethod()
    def calcular_alquiler(self):
        pass

class Apartamento(Inmueble):
    def __init__(self, direccion, codigo_postal, descripcion, habitaciones):
        super().__init(direccion, codigo_postal, descripcion)
        self.habitaciones = habitaciones

