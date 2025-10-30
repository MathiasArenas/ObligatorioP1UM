from entidades.persona import Persona
from utiles import Utiles

class Cliente(Persona):
    def __init__(self, nombre, apellido, documentoId, email, celular,nacionalidad,historial_vuelos=None):
        super().__init__(nombre, apellido, documentoId, email, celular)
        self.__nacionalidad = nacionalidad
        self.__historial_vuelos = historial_vuelos if None else []
        
    @property
    def nacionalidad(self): 
        return self.__nacionalidad
    @nacionalidad.setter
    def nacionalidad(self, nacionalidad): 
        self.__nacionalidad = nacionalidad
            
    @property
    def historial_vuelos(self): 
        return self.__historial_vuelos
    @historial_vuelos.setter
    def historial_vuelos(self, historial_vuelos):
        self.__historial_vuelos = historial_vuelos

    def registrar_persona(self):
        pass
    
    def __str__(self):
        return super().__str__() + f",\nNacionalidad: {self.nacionalidad}"

    def mostrar_cliente(self):
        Utiles.cls()
        print("\nCliente registrado exitosamente:")
        print(self)
        input("\nPresione Enter para continuar...")
