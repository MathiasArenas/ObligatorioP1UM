from entidades.persona import Persona
from entidades.roles import Roles
from utiles import Utiles
from excepciones.excepciones import Excepciones

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
    
    @staticmethod
    def registrar_persona(lista_tripulantes):
        nombre = Utiles.controlar_string (input ("Ingrese el nombre del tripulante: "))
        apellido = Utiles.controlar_string (input ("Ingrese el apellido del tripulante: "))
        documentoId = Utiles.controlar_numero (input ("Ingrese el documento de identidad del tripulante: "))
        for t in lista_tripulantes:
            if t.documentoId == documentoId:
                raise Excepciones.DatoDuplicadoError(f"El Tripulante con documento {documentoId} ya existe.")
            
        email = Utiles.controlar_email (input ("Ingrese el email del tripulante: "))
        celular = Utiles.controlar_numero (input ("Ingrese el celular del tripulante: "))
        rol = Utiles.controlar_string (input ("Ingrese el rol del tripulante (Piloto, Copiloto, Azafata): "))
        fecha_ingreso = Utiles.controlar_fecha (input ("Ingrese la fecha de ingreso del tripulante (DD/MM/AAAA): "))
        horas_vuelo = Utiles.controlar_numero (input ("Ingrese la cantidad de horas de vuelo acumuladas: "))
        tripulante = Tripulante (nombre, apellido, documentoId, email, celular, rol, fecha_ingreso, horas_vuelo) 
        return tripulante

    def __str__(self):
        return (
        super().__str__() +
        f",\nRol: {self.rol},"
        f"\nFecha de Ingreso: {self.fecha_ingreso}"
        )      

    def mostrar_tripulante(self):
        Utiles.cls()
        print("\nTripulante registrado exitosamente:")
        print(self)
        input("\nPresione Enter para continuar...")

    @staticmethod
    def mostrar_lista_tripulantes(lista_tripulantes):
        Utiles.cls()
        print("Lista de Tripulantes:")
        for tripulante in lista_tripulantes:
            print(f"Documento: {tripulante.documentoId}, Nombre: {tripulante.nombre}, Apellido: {tripulante.apellido}, Rol: {tripulante.rol}, Fecha de Ingreso: {tripulante.fecha_ingreso}")
    
    @staticmethod
    def buscar_tripulante_por_id(lista_tripulantes, documentoId):
        for tripulante in lista_tripulantes:
            if tripulante.documentoId == documentoId:
                return tripulante
        return None
    