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
    
    def registrar_persona(self):
        pass

    def __str__(self):
        return (
        super().__str__() +
        f",\nRol: {self.rol},"
        f"\nFecha de Ingreso: {self.fecha_ingreso}"
        )      

    def mostrar_tripulante(self):
        Utiles.cls()
        print("\Tripulante registrado exitosamente:")
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
    
    @staticmethod
    def validar_tripulante_para_vuelo(vuelo, lista_vuelos, lista_tripulantes):
        Utiles.cls()
        Tripulante.mostrar_lista_tripulantes(lista_tripulantes)

        documentoId = input("Ingrese el documento del tripulante: ")
        tripulante = Tripulante.buscar_tripulante_por_id(lista_tripulantes, documentoId)

        if not tripulante:
            raise Excepciones.ObjetoNoEncontradoError(f"No se encontró el tripulante con documento {documentoId}.")
        else:
            disponible = Tripulante.verificar_disponibilidad_tripulante(vuelo, documentoId, lista_vuelos)
            if not disponible:
                raise Excepciones.DatoDuplicadoError(f"El tripulante {documentoId} está asignado en vuelo {vuelo.id_vuelo} - destino {vuelo.destino}.")
            
        return tripulante
    
    @staticmethod
    def verificar_disponibilidad_tripulante(vuelo, documentoId, lista_vuelos):        
        for v in lista_vuelos:
            if vuelo.fecha == v.fecha:               
                for tripulante in v.tripulantes:
                    if tripulante.documentoId == documentoId:
                        return False
        return True
    