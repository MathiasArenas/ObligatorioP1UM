from persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, documentoId, email, celular,nacionalidad,historial_vuelos):
        super().__init__(nombre, apellido, documentoId, email, celular)
        self.__nacionalidad = nacionalidad
        self.__historial_vuelos = historial_vuelos
    def registrar_persona(self):
        self.__nombre = input ("Ingrese el nombre del cliente: ")
        self.__apellido = input ("Ingrese el apellido del cliente: ")
        self.__documentoId = input ("Ingrese el documento de identidad del cliente: ")
        self.__email = input ("Ingrese el email del cliente: ")
        self.__celular = input ("Ingrese el celular del cliente: ")
        self.__nacionalidad = input ("Ingrese la nacionalidad del cliente: ")
        self.__historial_vuelos = input ("Ingrese el historial de vuelos del cliente: ")
        return ("Cliente registrado", self.nombre, self.apellido, self.documentoId, self.email, self.celular, self.__nacionalidad, self.__historial_vuelos)


    # cliente1=Cliente("Juan", "Perez", "12345678", "mathias@mail","099882299", "Uruguayo", ["Vuelo1", "Vuelo2"])
    # print(cliente1.registrar_persona())