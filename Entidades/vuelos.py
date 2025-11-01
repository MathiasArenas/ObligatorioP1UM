from entidades.tripulante import Tripulante
from entidades.compania import Compania  
from utiles import Utiles

class Vuelos:
    def __init__(self, origen,destino,duracion,fecha,compania,capacidad,tipo_vuelo,id_vuelo,estado_vuelo):
        self.__origen = origen
        self.__destino = destino
        self.__duracion = duracion
        self.__fecha = fecha
        # self.__compania = Compania().validar_compania(compania)
        self.__compania = compania
        self.__capacidad = capacidad
        self.__tipo_vuelo = tipo_vuelo
        self.__id_vuelo = id_vuelo
        self.__estado_vuelo = estado_vuelo
        self.__tripulantes = []
        self.__clientes = []
        self.__equipajes = []

    @property
    def origen(self):    
        return self.__origen
    @origen.setter
    def origen(self, origen): 
        self.__origen = origen
    
    @property
    def destino(self):
        return self.__destino
    @destino.setter
    def destino(self, destino): 
        self.__destino = destino
    
    @property
    def duracion(self):
        return self.__duracion
    @duracion.setter
    def duracion(self, duracion): 
        self.__duracion = duracion
    
    @property
    def fecha(self):
        return self.__fecha
    @fecha.setter
    def fecha(self, fecha): 
        self.__fecha = fecha   
    @property
    def compania(self):
        return self.__compania
    @compania.setter
    def compania(self, compania): 
        self.__compania = Compania().validar_compania(compania)

    @property
    def capacidad(self):
        return self.__capacidad
    @capacidad.setter
    def capacidad(self, capacidad): 
        self.__capacidad = capacidad
    
    @property
    def tipo_vuelo(self):
        return self.__tipo_vuelo
    @tipo_vuelo.setter
    def tipo_vuelo(self, tipo_vuelo):
        self.__tipo_vuelo = tipo_vuelo

    @property
    def id_vuelo(self):
        return self.__id_vuelo
    @id_vuelo.setter
    def id_vuelo(self, id_vuelo):
        self.__id_vuelo = id_vuelo

    @property
    def estado_vuelo(self):
        return self.__estado_vuelo
    @estado_vuelo.setter
    def estado_vuelo(self, estado_vuelo):
        self.__estado_vuelo = estado_vuelo

    @property
    def tripulantes(self):
        return self.__tripulantes
    @tripulantes.setter
    def tripulantes(self,tripulantes):
        self.__tripulantes = tripulantes
       
    def registrar_vuelo():
        pass
    def validar_tipo_vuelo(tipo_vuelo):
        pass

    @staticmethod
    def mostrar_lista_vuelos(lista_vuelos):
        Utiles.cls()
        print("Lista de Vuelos:")
        for vuelo in lista_vuelos:
            print(f"ID Vuelo: {vuelo.id_vuelo}, Origen: {vuelo.origen}, Destino: {vuelo.destino}, Fecha: {vuelo.fecha}, Compañía: {vuelo.compania}, Estado: {vuelo.estado_vuelo}")
        
    @staticmethod
    def buscar_vuelo_por_id(lista_vuelos, id_vuelo):
        for vuelo in lista_vuelos:
            if vuelo.id_vuelo == id_vuelo:
                return vuelo
        return None

    @staticmethod
    def asignar_personal_vuelo(lista_vuelos, lista_tripulantes):
        
        Vuelos.mostrar_lista_vuelos(lista_vuelos)

        id_vuelo = input("Ingrese el ID del vuelo al que desea asignar un tripulante: ")
        vuelo = Vuelos.buscar_vuelo_por_id(lista_vuelos, id_vuelo)

        if not vuelo:
            print(f"No se encontró el vuelo con ID {id_vuelo}.")
            input("\nPresione Enter para continuar...")
            return
        
        Tripulante.mostrar_lista_tripulantes(lista_tripulantes)

        documentoId = input("Ingrese el documento del tripulante: ")
        tripulante = Tripulante.buscar_tripulante_por_id(lista_tripulantes, documentoId)

        if not tripulante:
            print(f"No se encontró el tripulante con documento {documentoId}.")
            input("\nPresione Enter para continuar...")
            return        
       
        lista_vuelos[lista_vuelos.index(vuelo)].tripulantes.append(tripulante)
        print(f"Tripulante {tripulante.nombre} asignado al vuelo {vuelo.id_vuelo}.")
        input("\nPresione Enter para continuar...")

    def asignar_cliente_a_vuelo(lista_clientes):
        pass
    def asignar_equipaje_a_vuelo(lista_equipajes):
        pass      
        

    def informe_pasajeros_por_vuelo(lista_vuelos):
        for vuelo in lista_vuelos:
            print(f"Vuelo ID: {vuelo.id_vuelo}")
            print("Pasajeros:")
            for cliente in vuelo.clientes:
                print(f" - {cliente.nombre}, {cliente.cedula}, {cliente.nacionalidad}, {cliente.cantidad_equipaje}")
            print("\n")