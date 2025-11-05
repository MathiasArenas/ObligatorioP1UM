from entidades.tripulante import Tripulante
from entidades.compania import Compania  
from utiles import Utiles
from Excepciones.excepciones import *

class Vuelos:
    def __init__(self, origen,destino,duracion,fecha,compania,capacidad,tipo_vuelo,id_vuelo,estado_vuelo):
        self.__origen = origen
        self.__destino = destino
        self.__duracion = duracion
        self.__fecha = fecha
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

    @property
    def clientes(self):
        return self.__clientes
    @clientes.setter
    def clientes(self,clientes):
        self.__clientes = clientes

    @property
    def equipajes(self):   
        return self.__equipajes
    
    @equipajes.setter
    def equipajes(self, equipajes): 
        self.__equipajes = equipajes

    def __str__(self):
        return (
            f"\nID Vuelo: {self.id_vuelo},"
            f"Origen: {self.origen},"
            f"Destino: {self.destino},"
            f"Duración: {self.duracion} horas,"
            f"Fecha: {self.fecha},"
            f"Compañía: {self.compania},"
            f"Capacidad: {self.capacidad} pasajeros,"
            f"Tipo de Vuelo: {self.tipo_vuelo},"
            f"Estado del Vuelo: {self.estado_vuelo},"
            f"Cantidad de Tripulantes Asignados: {len(self.tripulantes)},"
            f"Cantidad de Clientes Asignados: {len(self.clientes)},"
            f"Cantidad de Equipajes Asignados: {len(self.equipajes)}\n"
        )
    
    def mostrar_vuelo(self):
        print(self)

    def registrar_vuelo():
        pass
    def validar_tipo_vuelo(tipo_vuelo):
        pass

    @staticmethod
    def mostrar_lista_vuelos(lista_vuelos):
        Utiles.cls()
        print("Lista de Vuelos:")
        for vuelo in lista_vuelos:
            Vuelos.mostrar_vuelo(vuelo)
        
   
    @staticmethod
    def buscar_vuelo_por_id(lista_vuelos):
        Utiles.cls()
        Vuelos.mostrar_lista_vuelos(lista_vuelos)
        id_vuelo = Utiles.controlar_string(input("Ingrese el ID del vuelo: "))    
        
        for vuelo in lista_vuelos:
            if vuelo.id_vuelo == id_vuelo:
                return vuelo
            
        if not lista_vuelos:
            print("No hay vuelos registrados.")
            return
        Utiles.cls()
        print("\n=== Lista de vuelos disponibles para cancelar ===")
        if not lista_vuelos:
            print("No hay vuelos registrados.")
            input("\nPresione Enter para continuar...")
            return
        for vuelo in lista_vuelos:
            print(f"ID Vuelo: {vuelo.id_vuelo} | Origen: {vuelo.origen} | Destino: {vuelo.destino} | Fecha: {vuelo.fecha} | Compañía: {vuelo.compania.nombre} | Estado: {vuelo.estado_vuelo}")
        vuelo_cancelar_id = input("\nIngrese el ID del vuelo a cancelar: ")
        vuelo_cancelar = next((v for v in lista_vuelos if v.id_vuelo == vuelo_cancelar_id), None)
        if not vuelo_cancelar:
            print(f"\n[ERROR] No se encontró el vuelo con ID '{vuelo_cancelar_id}'. Volviendo al menú principal.")
            input("\nPresione Enter para continuar...")
            return
        vuelos_similares = [
            v for v in lista_vuelos
            if v.origen == vuelo_cancelar.origen and
               v.destino == vuelo_cancelar.destino and
               v.capacidad >= vuelo_cancelar.capacidad and
               v.id_vuelo != vuelo_cancelar.id_vuelo and
               v.estado_vuelo != "Cancelado"
        ]
        if vuelos_similares:
            print("\nVuelos similares disponibles para reubicación:")
            for vuelo in vuelos_similares:
                print(f"ID Vuelo: {vuelo.id_vuelo} | Origen: {vuelo.origen} | Destino: {vuelo.destino} | Fecha: {vuelo.fecha} | Compañía: {vuelo.compania.nombre} | Estado: {vuelo.estado_vuelo}")
            nuevo_vuelo_id = input("\nIngrese el ID del vuelo para reubicar a los pasajeros: ")
            nuevo_vuelo = next((v for v in vuelos_similares if v.id_vuelo == nuevo_vuelo_id), None)
            if nuevo_vuelo:
                vuelo_cancelar.estado_vuelo = "Cancelado"
                print(f"Vuelo {vuelo_cancelar.id_vuelo} cancelado. Pasajeros reubicados al vuelo {nuevo_vuelo.id_vuelo}.")
            else:
                print(f"No se encontró el vuelo de reubicación con ID {nuevo_vuelo_id}.")
        else:
            vuelo_cancelar.estado_vuelo = "Cancelado"
            print(f"Vuelo {vuelo_cancelar.id_vuelo} cancelado. No hay vuelos similares para reubicar a los pasajeros.")
        input("\nPresione Enter para continuar...")
        if vuelo.id_vuelo.upper() == id_vuelo.upper():
            return vuelo            

        raise objetoNoEncontradoError("Vuelo no encontrado.")     

    @staticmethod
    def asignar_personal_vuelo(lista_vuelos, lista_tripulantes):

        try:
            vuelo = Vuelos.buscar_vuelo_por_id(lista_vuelos)        
        except Exception as e:
            print(str(e))
            input("\nPresione Enter para continuar...")
            return
        
        try:
            tripulante = Tripulante.validar_tripulante_para_vuelo(vuelo, lista_vuelos, lista_tripulantes)
        except Exception as e:
            print(str(e))
            input("\nPresione Enter para continuar...")
            return

        lista_vuelos[lista_vuelos.index(vuelo)].tripulantes.append(tripulante)

        print(f"Tripulante {tripulante.nombre} asignado al vuelo {vuelo.id_vuelo}.\n")
        print(vuelo)
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

    @staticmethod
    def visualizar_vuelos(lista_vuelos):
        Vuelos.mostrar_lista_vuelos(lista_vuelos)
        input("\nPresione Enter para continuar...")

        
    def informe_personal_asignado(lista_vuelos):
        Utiles.cls()
        print("Informe de personal asignado por vuelo:")
        for vuelo in lista_vuelos:
            print(f"\nVuelo ID: {vuelo.id_vuelo}, Origen: {vuelo.origen}, Destino: {vuelo.destino}, Fecha: {vuelo.fecha}")
            if vuelo.tripulantes:
                for tripulante in vuelo.tripulantes:
                    print(f"  - Tripulante Documento: {tripulante.documentoId}, Nombre: {tripulante.nombre} {tripulante.apellido}, Rol: {tripulante.rol}")
            else:
                print("  No hay tripulantes asignados a este vuelo.")
        input("\nPresione Enter para continuar...")

    def informe_vuelos_por_compania(lista_vuelos):
        Utiles.cls()
        companias_vuelos = {}
        for vuelo in lista_vuelos:
            nombre_compania = vuelo.compania.nombre
            if nombre_compania not in companias_vuelos:
                companias_vuelos[nombre_compania] = []
            companias_vuelos[nombre_compania].append(vuelo)

        print("Informe de vuelos por compañía:")
        for compania, vuelos in companias_vuelos.items():
            print(f"\nCompañía: {compania}")
            for vuelo in vuelos:
                print(f"  - Vuelo ID: {vuelo.id_vuelo}, Origen: {vuelo.origen}, Destino: {vuelo.destino}, Fecha: {vuelo.fecha}, Estado: {vuelo.estado_vuelo}")
        input("\nPresione Enter para continuar...")

    def informe_vuelos_cancelados(lista_vuelos):
        Utiles.cls()
        print("Informe de vuelos cancelados:")
        vuelos_cancelados = [vuelo for vuelo in lista_vuelos if vuelo.estado_vuelo == "Cancelado"]
        if not vuelos_cancelados:
            print("No hay vuelos cancelados.")
        else:
            for vuelo in vuelos_cancelados:
                print(f"Vuelo ID: {vuelo.id_vuelo}, Origen: {vuelo.origen}, Destino: {vuelo.destino}, Fecha: {vuelo.fecha}, Compañía: {vuelo.compania.nombre}, Causa de Cancelación: {getattr(vuelo, 'causa_cancelacion', 'N/A')}")
        input("\nPresione Enter para continuar...")

    @staticmethod
    def cancelar_vuelo(lista_vuelos):
        Utiles.cls()
        print("\n=== Lista de vuelos disponibles para cancelar ===")
        if not lista_vuelos:
            print("No hay vuelos registrados.")
            input("\nPresione Enter para continuar...")
            return
        
        for vuelo in lista_vuelos:
            print(f"ID Vuelo: {vuelo.id_vuelo} | Origen: {vuelo.origen} | Destino: {vuelo.destino} | Fecha: {vuelo.fecha} | Compañía: {vuelo.compania.nombre} | Estado: {vuelo.estado_vuelo}")
        
        vuelo_cancelar_id = input("\nIngrese el ID del vuelo a cancelar: ")
        vuelo_cancelar = next((v for v in lista_vuelos if v.id_vuelo == vuelo_cancelar_id), None)
        
        if not vuelo_cancelar:
            print(f"\n[ERROR] No se encontró el vuelo con ID '{vuelo_cancelar_id}'. Volviendo al menú principal.")
            input("\nPresione Enter para continuar...")
            return
        
        # Buscar vuelos similares para reubicación
        vuelos_similares = [
            v for v in lista_vuelos
            if v.origen == vuelo_cancelar.origen and
               v.destino == vuelo_cancelar.destino and
               v.capacidad >= vuelo_cancelar.capacidad and
               v.id_vuelo != vuelo_cancelar.id_vuelo and
               v.estado_vuelo != "Cancelado"
        ]
        
        if not vuelos_similares:
            print(f"\n[ERROR] No se puede cancelar el vuelo {vuelo_cancelar.id_vuelo}. Debe haber al menos 1 vuelo disponible para reasignar a los pasajeros.")
            input("\nPresione Enter para continuar...")
            return
        
        print("\nVuelos similares disponibles para reubicación:")
        for vuelo in vuelos_similares:
            print(f"ID Vuelo: {vuelo.id_vuelo} | Origen: {vuelo.origen} | Destino: {vuelo.destino} | Fecha: {vuelo.fecha} | Compañía: {vuelo.compania.nombre} | Estado: {vuelo.estado_vuelo}")
        
        nuevo_vuelo_id = input("\nIngrese el ID del vuelo para reubicar a los pasajeros: ")
        nuevo_vuelo = next((v for v in vuelos_similares if v.id_vuelo == nuevo_vuelo_id), None)
        
        if nuevo_vuelo:
            vuelo_cancelar.estado_vuelo = "Cancelado"
            print(f"\nVuelo {vuelo_cancelar.id_vuelo} cancelado. Pasajeros reubicados al vuelo {nuevo_vuelo.id_vuelo}.")
        else:
            print(f"\n[ERROR] No se encontró el vuelo de reubicación con ID '{nuevo_vuelo_id}'.")
        
        input("\nPresione Enter para continuar...")

