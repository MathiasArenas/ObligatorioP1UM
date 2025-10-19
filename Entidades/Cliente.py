from persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, documentoId, email, celular,nacionalidad,historial_vuelos):
        super().__init__(nombre, apellido, documentoId, email, celular)
        self.__nacionalidad = nacionalidad
        self.__historial_vuelos = historial_vuelos
    def registrar_persona(self):
        nombre = input ("Ingrese el nombre del cliente: ")
        apellido = input ("Ingrese el apellido del cliente: ")
        documentoId = input ("Ingrese el documento de identidad del cliente: ")
        email = input ("Ingrese el email del cliente: ")
        celular = input ("Ingrese el celular del cliente: ")
        nacionalidad = input ("Ingrese la nacionalidad del cliente: ")
        historial_vuelos = input ("Ingrese el historial de vuelos del cliente: ")
        return ("Cliente registrado", self.nombre, self.apellido, self.documentoId, self.email, self.celular, self.__nacionalidad, self.__historial_vuelos)


