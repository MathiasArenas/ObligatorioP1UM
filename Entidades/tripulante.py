from persona import Persona
from roles import Roles

class Tripulante(Persona): 
    def __init__(self, nombre, apellido, documentoId, email, celular, rol, fecha_ingreso, horas_vuelo):
        super().__init__(nombre, apellido, documentoId, email, celular)
        self.__rol = Roles().validar_rol(rol)
        self.__fecha_ingreso = fecha_ingreso
        self.__horas_vuelo = horas_vuelo
        @property
        def rol(self):
            return self.__rol
        @rol.setter
        def rol(self, rol):
            self.__rol = Roles().validar_rol(rol)
        @property
        def fecha_ingreso(self):
            return self.__fecha_ingreso
        @fecha_ingreso.setter
        def fecha_ingreso(self, fecha_ingreso):
            self.__fecha_ingreso = fecha_ingreso
        @property
        def horas_vuelo(self):
            return self.__horas_vuelo
        @horas_vuelo.setter
        def horas_vuelo(self, horas_vuelo):
            self.__horas_vuelo = horas_vuelo
    
    def registrar_persona():
        nombre = input ("Ingrese el nombre del tripulante: ")
        apellido = input ("Ingrese el apellido del tripulante: ")
        documentoId = input ("Ingrese el documento de identidad del tripulante: ")
        email = input ("Ingrese el email del tripulante: ")
        celular = input ("Ingrese el celular del tripulante: ")
        rol = input ("Ingrese el rol del tripulante (Piloto, Copiloto, Azafata): ")
        fecha_ingreso = input ("Ingrese la fecha de ingreso del tripulante (DD/MM/AAAA): ")
        horas_vuelo = input ("Ingrese las horas de vuelo del tripulante: ")        
        return ("Tripulante registrado", nombre, apellido, documentoId, email, celular, rol, fecha_ingreso, horas_vuelo)
        
