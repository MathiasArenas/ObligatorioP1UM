from entidades.tripulante import Tripulante
from entidades.compania import Compania  
from utiles import Utiles
from excepciones.excepciones import Excepciones as exc
import datetime

class Vuelos:
    def __init__(self, origen,destino,duracion,fecha,compania,capacidad,tipo_vuelo,id_vuelo,estado_vuelo,
                 tickets=None):
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
        self.__tickets = []

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

    @property
    def tickets(self):   
        return self.__tickets
    @tickets.setter
    def tickets(self, tickets): 
        self.__tickets = tickets

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
            f"Cantidad de Equipajes Asignados: {len(self.equipajes)},"
            f"Tickets vendidos: {len(self.__tickets)}\n"
        )
    
    def mostrar_vuelo(self):
        print(self)

    def registrar_vuelo(lista_companias):
        
        if not lista_companias:
            print("No hay compañías registradas. Debe crear al menos una compañía antes de crear un vuelo.")
            input("\nPresione Enter para continuar...")
            return None

        origen = input("Ingrese el origen del vuelo: ")
        destino = input("Ingrese el destino del vuelo: ")
        duracion = input("Ingrese la duración del vuelo (en horas): ")
        fecha = input("Ingrese la fecha del vuelo (DD/MM/AAAA): ")

        print("\nCompañías disponibles:")
        for idx, comp in enumerate(lista_companias):
            print(f"{idx + 1}. {comp.nombre} ({comp.codigo})") 

        seleccion = input("Seleccione el número de la compañía: ")
        try:
            seleccion = int(seleccion)
            compania = lista_companias[seleccion - 1]
        except (ValueError, IndexError):
            raise ValueError("Selección inválida de compañía.")

        capacidad = input("Ingrese la capacidad del vuelo: ")
        tipo_vuelo = input("Ingrese el tipo de vuelo (Nacional/Internacional): ")
        id_vuelo = Utiles().generar_id_unico()
        estado_vuelo = "Activo"

        tipo_vuelo = Vuelos.validar_tipo_vuelo(tipo_vuelo)

        vuelo = Vuelos(
            origen=origen,
            destino=destino,
            duracion=duracion,
            fecha=fecha,
            compania=compania,
            capacidad=capacidad,
            tipo_vuelo=tipo_vuelo,
            id_vuelo=id_vuelo,
            estado_vuelo=estado_vuelo
        )

        print(f"\nVuelo {id_vuelo} registrado correctamente.")
        return vuelo
    
    @staticmethod
    def validar_tipo_vuelo(tipo_vuelo):
        tipos_validos = ['Nacional', 'Internacional']
        if tipo_vuelo in tipos_validos:
            return tipo_vuelo
        else:
            raise ValueError(f"Tipo de vuelo inválido. Los tipos válidos son: {', '.join(tipos_validos)}")

    @staticmethod
    def mostrar_lista_vuelos(lista_vuelos):
        Utiles.cls()
        print("Lista de Vuelos:")
        for vuelo in lista_vuelos:
            Vuelos.mostrar_vuelo(vuelo)   
    
    @staticmethod
    def mostrar_vuelo_para_seleccion(lista_vuelos):
        Utiles.cls()
        print("Vuelos disponibles:")
        for vuelo in lista_vuelos:
            if vuelo.estado_vuelo != "Cancelado" and vuelo.fecha > datetime.datetime.now().strftime("%d/%m/%Y"):
                print(f"ID Vuelo: {vuelo.id_vuelo}, Origen: {vuelo.origen}, Destino: {vuelo.destino}, Fecha: {vuelo.fecha}")
        id_vuelo = input("Ingrese el ID del vuelo que desea seleccionar: ")
        return id_vuelo
   
    
    @staticmethod
    def buscar_vuelo_por_id(lista_vuelos, id_vuelo):
        if not lista_vuelos:
            raise exc.VueloNoEncontradoError("No hay vuelos registrados.")

        for vuelo in lista_vuelos:
            if vuelo.id_vuelo.upper() == id_vuelo.upper():
                return vuelo

        raise exc.VueloNoEncontradoError("Vuelo no encontrado.")    

    @staticmethod
    def asignar_personal_vuelo(lista_vuelos, lista_tripulantes,vuelo):
        
        try:
            tripulante = Tripulante.validar_tripulante_para_vuelo(vuelo, lista_vuelos, lista_tripulantes)
        except exc.DatoDuplicadoError as e:
            print(e.mensaje)
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

    
    def agregar_ticket(self, ticket):
        if len(self.__tickets) >= self.__capacidad:
            raise exc.CapacidadExcedidaError("No se pueden agregar más tickets, capacidad máxima alcanzada.")
        
        self.__tickets.append(ticket)
       
