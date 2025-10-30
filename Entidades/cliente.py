from entidades.persona import Persona

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
        return (f"Cliente: {self.nombre} {self.apellido}, "
                f"Documento: {self.documentoId}, Email: {self.email}, "
                f"Celular: {self.celular}, Nacionalidad: {self.nacionalidad}")