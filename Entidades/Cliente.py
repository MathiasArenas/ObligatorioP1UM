from Persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, documentoId, email, celular,nacionalidad,historial_vuelos):
        super().__init__(nombre, apellido, documentoId, email, celular)
        self.__nacionalidad = nacionalidad
        self.__historial_vuelos = historial_vuelos
    def registrar_persona(self):
        return ("Cliente registrado", self.nombre, self.apellido, self.documentoId, self.email, self.celular, self.__nacionalidad, self.__historial_vuelos)


