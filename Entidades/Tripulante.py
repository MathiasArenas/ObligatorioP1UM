from persona import Persona
from roles import Roles

class Tripulante(Persona): 
    def __init__(self, nombre, apellido, documentoId, email, celular, rol, fecha_ingreso, horas_vuelo):
        super().__init__(nombre, apellido, documentoId, email, celular)
        self.__rol = Roles().validar_rol(rol)
        self.__fecha_ingreso = fecha_ingreso
        self.__horas_vuelo = horas_vuelo
    
    def registrar_persona(self):
        self.__nombre = input ("Ingrese el nombre del tripulante: ")
        self.__apellido = input ("Ingrese el apellido del tripulante: ")
        self.__documentoId = input ("Ingrese el documento de identidad del tripulante: ")
        self.__email = input ("Ingrese el email del tripulante: ")
        self.__celular = input ("Ingrese el celular del tripulante: ")
        self.__rol = input ("Ingrese el rol del tripulante (Piloto, Copiloto, Azafata): ")
        self.__fecha_ingreso = input ("Ingrese la fecha de ingreso del tripulante (DD/MM/AAAA): ")
        self.__horas_vuelo = input ("Ingrese las horas de vuelo del tripulante: ")        
        return ("Tripulante registrado", self.nombre, self.apellido, self.documentoId, self.email, self.celular, self.__rol, self.__fecha_ingreso, self.__horas_vuelo)
        
