from persona import Persona
from roles import Roles

class Tripulante(Persona): 
    def __init__(self, nombre, apellido, documentoId, email, celular, rol, fecha_ingreso, horas_vuelo):
        super().__init__(nombre, apellido, documentoId, email, celular)
        self.__rol = Roles().validar_rol(rol)
        self.__fecha_ingreso = fecha_ingreso
        self.__horas_vuelo = horas_vuelo
    
    def registrar_persona(self):
        return ("Tripulante registrado", self.nombre, self.apellido, self.documentoId, self.email, self.celular, self.__rol, self.__fecha_ingreso, self.__horas_vuelo)
        
    # tripulante1=Tripulante("Ana", "Gomez", "87654321", "ana@mail","098877766", "Piloto", "2020-01-15", 1500)
    # print(tripulante1.registrar_persona())
