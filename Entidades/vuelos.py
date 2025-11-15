from entidades.compania import Compania  
from utiles import Utiles
from excepciones.excepciones import Excepciones as exc

class Vuelos:
    def __init__(self, origen,destino,duracion,fecha,compania,capacidad,tipo_vuelo,id_vuelo,estado_vuelo,
                 tickets=None, causa_cancelacion=None, fecha_cancelacion=None):
        self.__origen = origen
        self.__destino = destino
        self.__duracion = duracion
        self.__fecha = fecha
        self.__compania = compania
        self.__capacidad_total = int(capacidad)
        self.__tipo_vuelo = tipo_vuelo
        self.__id_vuelo = id_vuelo
        self.__estado_vuelo = estado_vuelo
        self.__tripulantes = []
        self.__equipajes = []
        self.__tickets = []
        self.__clientes = []
        self.__causa_cancelacion = causa_cancelacion
        self.__fecha_cancelacion = fecha_cancelacion
        
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
        return self.__capacidad_total
    @capacidad.setter
    def capacidad(self, capacidad): 
        self.__capacidad_total = int(capacidad)

    @property
    def capacidad_total(self):
        return self.__capacidad_total

    @property
    def asientos_libres(self):
        ocupados = len([t for t in self.__tickets if t.estado != "Cancelado"])
        return max(self.__capacidad_total - ocupados, 0)
    
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
        
    @property
    def causa_cancelacion(self):
        return self.__causa_cancelacion
    
    @causa_cancelacion.setter
    def causa_cancelacion(self, causa_cancelacion):
        self.__causa_cancelacion = causa_cancelacion

    @property
    def fecha_cancelacion(self):
        return self.__fecha_cancelacion

    @fecha_cancelacion.setter
    def fecha_cancelacion(self, fecha_cancelacion):
        self.__fecha_cancelacion = fecha_cancelacion

    def __str__(self):
        return (
            f"\nID Vuelo: {self.id_vuelo},"
            f"Origen: {self.origen},"
            f"Destino: {self.destino},"
            f"Duración: {self.duracion} horas,"
            f"Fecha: {self.fecha},"
            f"Compañía: {getattr(self.compania, 'nombre', self.compania)},"
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

        origen = Utiles.controlar_string (input("Ingrese el origen del vuelo: "))
        destino = Utiles.controlar_string (input("Ingrese el destino del vuelo: "))
        duracion = Utiles.controlar_numero (input("Ingrese la duración del vuelo (en horas): "))
        fecha = Utiles.controlar_fecha (input("Ingrese la fecha del vuelo (DD/MM/AAAA): "))

        print("\nCompañías disponibles:")
        for idx, comp in enumerate(lista_companias):
            print(f"{idx + 1}. {comp.nombre} ({comp.codigo})") 

        seleccion = input("Seleccione el número de la compañía: ")
        try:
            seleccion = int(seleccion)
            compania = lista_companias[seleccion - 1]
        except (ValueError, IndexError):
            raise ValueError("Selección inválida de compañía.")

        capacidad = Utiles.controlar_numero (input("Ingrese la capacidad del vuelo: "))
        tipo_vuelo = Utiles.controlar_string (input("Ingrese el tipo de vuelo (Nacional/Internacional): "))
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
        tipos_validos = { 'nacional': 'Nacional', 'internacional': 'Internacional' }
        clave = tipo_vuelo.lower()
        if clave in tipos_validos:
            return tipos_validos[clave]
        else:
            raise ValueError(f"Tipo de vuelo inválido. Los tipos válidos son: {', '.join(tipos_validos)}")
    
    @staticmethod
    def mostrar_lista_vuelos(lista_vuelos):
        Utiles.cls()
        print("Lista de Vuelos:")

        if not lista_vuelos:
            print("No hay vuelos registrados.")
            return

        for index, vuelo in enumerate(lista_vuelos, start=1):
            print(
                f"{index}. ID: {vuelo.id_vuelo} | "
                f"{vuelo.origen} → {vuelo.destino} | "
                f"Fecha: {vuelo.fecha} | Estado: {vuelo.estado_vuelo}"
            )
    
    @staticmethod
    def mostrar_vuelo_para_seleccion(lista_vuelos):
        Utiles.cls()
        print("Seleccione un vuelo:\n")

        vuelos_validos = [
            v for v in lista_vuelos
            if v.estado_vuelo != "Cancelado"
        ]

        if not vuelos_validos:
            print("No hay vuelos disponibles.")
            return None

        for index, vuelo in enumerate(vuelos_validos, start=1):
            print(f"{index}. {vuelo.origen} → {vuelo.destino} | Fecha: {vuelo.fecha} | ID: {vuelo.id_vuelo}")

        while True:
            seleccion = input("\nIngrese el número del vuelo: ")

            if not seleccion.isdigit():
                print("Debe ingresar un número.")
                continue

            seleccion = int(seleccion)

            if 1 <= seleccion <= len(vuelos_validos):
                return vuelos_validos[seleccion - 1]
            else:
                print("Número fuera de rango. Intente nuevamente.")
    
    
    @staticmethod
    def buscar_vuelo_por_id(lista_vuelos, id_vuelo):
        if not lista_vuelos:
            raise exc.VueloNoEncontradoError("No hay vuelos registrados.")

        for vuelo in lista_vuelos:
            if vuelo.id_vuelo.upper() == id_vuelo.upper():
                return vuelo

        raise exc.VueloNoEncontradoError("Vuelo no encontrado.")
    
    @staticmethod
    def seleccionar_tripulante_por_rol(lista_tripulantes, vuelo, rol):
        disponibles = [t for t in lista_tripulantes if t.rol == rol and t not in vuelo.tripulantes]
        if not disponibles:
            print(f"No hay {rol} disponible para asignar.")
            return None

        print(f"\nTripulantes disponibles para {rol}:")
        for i, t in enumerate(disponibles, start=1):
            print(f"{i}. {t.nombre} - Documento: {t.documentoId}")

        try:
            indice = int(input(f"Seleccione el número del {rol}: "))
            return disponibles[indice - 1]
        except (ValueError, IndexError):
            print("Selección inválida.")
            return None


    @staticmethod
    def asignar_personal_vuelo(lista_tripulantes, vuelo):
        roles_requeridos = ["Piloto", "Copiloto", "Azafata"]
        continuar = True

        while continuar:
            roles_actuales = {t.rol for t in vuelo.tripulantes}
            print(f"\nRoles asignados actualmente: {roles_actuales}")

            if all(rol in roles_actuales for rol in roles_requeridos):
                opcion = input("El vuelo ya tiene al menos un Piloto, Copiloto y Azafata. ¿Desea seguir? (S/N): ").strip().upper()
                continuar = (opcion == "S")
                if not continuar:
                    print("Asignación finalizada.")
                    continue

            print("\nAsignar Tripulante al Vuelo")
            print("1. Piloto\n2. Copiloto\n3. Azafata")
            opcion_rol = input("Ingrese el número del rol a asignar: ").strip()

            match opcion_rol:
                case "1":
                    rol = "Piloto"
                    print("Seleccione un Piloto:")
                    tripulante = Vuelos.seleccionar_tripulante_por_rol(lista_tripulantes, vuelo, rol)
                case "2":
                    rol = "Copiloto"
                    print("Seleccione un Copiloto:")
                    tripulante = Vuelos.seleccionar_tripulante_por_rol(lista_tripulantes, vuelo, rol)
                case "3":
                    rol = "Azafata"
                    print("Seleccione una Azafata:")
                    tripulante = Vuelos.seleccionar_tripulante_por_rol(lista_tripulantes, vuelo, rol)
                case _:
                    print("Rol inválido.")
                    continue

            if tripulante:
                vuelo.tripulantes.append(tripulante)
                
                try:
                    tripulante.horas_vuelo = float(tripulante.horas_vuelo) + float(vuelo.duracion)
                except Exception:
                    pass
                print(f"{rol} {tripulante.nombre} asignado al vuelo {vuelo.id_vuelo}.")
            else:
                print("\nNo se asignó ningún tripulante.")

            continuar = input("¿Desea asignar otro tripulante? (S/N): ").strip().upper() == "S"

        print("\nAsignación de tripulación finalizada.")
        input("Presione Enter para continuar...")


    def asignar_cliente_a_vuelo(lista_clientes):
        pass
    
    def asignar_equipaje_a_vuelo(self, equipaje):
        self.__equipajes.append(equipaje)     
    
    @staticmethod
    def informe_pasajeros_por_vuelo(lista_vuelos):
        Utiles.cls()
        print("Informe de pasajeros por vuelo:")
        for vuelo in lista_vuelos:
            print(f"\nVuelo {vuelo.id_vuelo} ({vuelo.origen} → {vuelo.destino})")
            if not vuelo.tickets:
                print("  - Sin tickets")
                continue
            for ticket in vuelo.tickets:
                if ticket.estado == "Cancelado":
                    continue
                cliente = ticket.cliente
                equipajes = [e for e in vuelo.equipajes if e.pasajero.documentoId == cliente.documentoId]
                print(f"  - Asiento {getattr(ticket, 'numero_asiento', 'N/A')}: {cliente.nombre} ({cliente.documentoId}), {getattr(cliente, 'nacionalidad', 'N/A')}, {len(equipajes)} equipaje(s)")
        input("\nPresione Enter para continuar...")

    @staticmethod
    def visualizar_vuelos(lista_vuelos):
        Utiles.cls()
        
        if not lista_vuelos:
            print("No hay vuelos registrados.")
            input("\nPresione Enter para continuar...")
            return
        
        print("Seleccione un vuelo para ver detalles:\n")
        
        for index, vuelo in enumerate(lista_vuelos, start=1):
            print(f"{index}. ID: {vuelo.id_vuelo} | {vuelo.origen} → {vuelo.destino} | Fecha: {vuelo.fecha} | Estado: {vuelo.estado_vuelo}")
        
        while True:
            seleccion = input("\nIngrese el número del vuelo (0 para volver): ")
            
            if seleccion == "0":
                return
                
            if not seleccion.isdigit():
                print("Debe ingresar un número.")
                continue
            
            seleccion = int(seleccion)
            
            if 1 <= seleccion <= len(lista_vuelos):
                vuelo = lista_vuelos[seleccion - 1]
                break
            else:
                print("Número fuera de rango. Intente nuevamente.")
        
        Utiles.cls()
        print("Detalle del vuelo:")
        print("-"*60)
        print(f"Vuelo {vuelo.id_vuelo} | {vuelo.origen} → {vuelo.destino} | Fecha: {vuelo.fecha} | Estado: {vuelo.estado_vuelo}")
        print(f"Compañía: {getattr(vuelo.compania,'nombre', vuelo.compania)} | Capacidad Total: {vuelo.capacidad_total} | Asientos libres: {vuelo.asientos_libres}")
        
        if vuelo.tripulantes:
            roles = {"Piloto": [], "Copiloto": [], "Azafata": []}
            for t in vuelo.tripulantes:
                roles.setdefault(t.rol, []).append(f"{t.nombre} {t.apellido}")
            print("Tripulación:")
            for rol, personas in roles.items():
                if personas:
                    print(f"  {rol}: "+ ", ".join(personas))
        else:
            print("Sin tripulación asignada.")
        
        activos = [t for t in vuelo.tickets if t.estado != "Cancelado"]
        if activos:
            print("Pasajeros:")
            for t in sorted(activos, key=lambda x: (x.numero_asiento or 0)):
                c = t.cliente
                print(f"  Asiento {t.numero_asiento}: {c.nombre} {c.apellido} ({c.documentoId})")
        else:
            print("Sin pasajeros.")
        
        print("-"*60)
        input("\nPresione Enter para continuar...")

    @staticmethod
    def informe_personal_asignado(lista_vuelos):
        Utiles.cls()
        print("Informe de personal asignado por vuelo:")
        for vuelo in lista_vuelos:
            print(f"\nVuelo ID: {vuelo.id_vuelo}, Origen: {vuelo.origen}, Destino: {vuelo.destino}, Fecha: {vuelo.fecha}")
            if vuelo.tripulantes:
                for tripulante in vuelo.tripulantes:
                    print(f"  - Documento: {tripulante.documentoId}, Nombre: {tripulante.nombre} {tripulante.apellido}, Rol: {tripulante.rol}")
            else:
                print("  No hay tripulantes asignados a este vuelo.")
        input("\nPresione Enter para continuar...")

    @staticmethod
    def informe_vuelos_por_compania(lista_vuelos):
        Utiles.cls()
        companias_vuelos = {}
        for vuelo in lista_vuelos:
            nombre_compania = getattr(vuelo.compania, 'nombre', 'N/A')
            if nombre_compania not in companias_vuelos:
                companias_vuelos[nombre_compania] = []
            companias_vuelos[nombre_compania].append(vuelo)

        print("Informe de vuelos por compañía:")
        for compania, vuelos in companias_vuelos.items():
            print(f"\nCompañía: {compania}")
            for vuelo in vuelos:
                print(f"  - Vuelo ID: {vuelo.id_vuelo}, Origen: {vuelo.origen}, Destino: {vuelo.destino}, Fecha: {vuelo.fecha}, Estado: {vuelo.estado_vuelo}")
        input("\nPresione Enter para continuar...")

    @staticmethod
    def informe_vuelos_cancelados(lista_vuelos):
        Utiles.cls()
        print("Informe de vuelos cancelados:")
        vuelos_cancelados = [vuelo for vuelo in lista_vuelos if vuelo.estado_vuelo == "Cancelado"]
        if not vuelos_cancelados:
            print("No hay vuelos cancelados.")
        else:
            for vuelo in vuelos_cancelados:
                pasajeros_afectados = sum(1 for t in vuelo.tickets if t.estado != "Cancelado")
                print(
                    f"Vuelo ID: {vuelo.id_vuelo}, Origen: {vuelo.origen}, Destino: {vuelo.destino}, "
                    f"Fecha: {vuelo.fecha}, Compañía: {getattr(vuelo.compania, 'nombre', 'N/A')}, "
                    f"Causa: {getattr(vuelo, 'causa_cancelacion', 'N/A')}, Pasajeros afectados: {pasajeros_afectados}"
                )
        input("\nPresione Enter para continuar...")

    
    def agregar_ticket(self, ticket):
        if len([t for t in self.__tickets if t.estado != "Cancelado"]) >= self.__capacidad_total:
            raise exc.CapacidadExcedidaError("No se pueden agregar más tickets, capacidad máxima alcanzada.")
        self.__tickets.append(ticket)

    def listar_tickets_por_vuelo(self):
        print(f"\nTickets para el vuelo {self.id_vuelo}:")
        tickets_activos = [t for t in self.tickets if t.estado != "Cancelado"]
        tickets_cancelados = [t for t in self.tickets if t.estado == "Cancelado"]
        
        if tickets_activos:
            print("\n--- Tickets Activos ---")
            for ticket in tickets_activos:
                print(ticket)
        else:
            print("  No hay tickets activos.")
            
        if tickets_cancelados:
            print("\n--- Tickets Cancelados ---")
            for ticket in tickets_cancelados:
                print(ticket)
            
    def listar_equipajes_por_vuelo(self):
        print(f"\nEquipajes para el vuelo {self.id_vuelo}:")
        for equipaje in self.equipajes:
            print(equipaje)
            
    @staticmethod        
    def cancelar_vuelo(lista_vuelos):
        if not lista_vuelos:
            print("No hay vuelos registrados.")
            return

        Vuelos.mostrar_lista_vuelos(lista_vuelos)
        id_vuelo = input("\nIngrese el ID del vuelo a cancelar: ")
        try:
            origen = Vuelos.buscar_vuelo_por_id(lista_vuelos, id_vuelo)
        except exc.VueloNoEncontradoError as e:
            print(str(e))
            input("\nPresione Enter para continuar...")
            return

        if origen.estado_vuelo == "Cancelado":
            print("El vuelo ya está cancelado.")
            input("\nPresione Enter para continuar...")
            return

        print("\nVuelos disponibles para reasignar (excluye cancelados y el mismo vuelo):")
        destinos = [v for v in lista_vuelos if v.id_vuelo != origen.id_vuelo and v.estado_vuelo != "Cancelado"]
        if not destinos:
            print("No hay vuelos destino disponibles para la reasignación.")
            input("\nPresione Enter para continuar...")
            return
        for i, v in enumerate(destinos, start=1):
            print(f"{i}. {v.id_vuelo} | {v.origen} → {v.destino} | {v.fecha} | Libres: {v.asientos_libres}")
        try:
            idx = int(input("Seleccione el número del vuelo destino: "))
            destino = destinos[idx-1]
        except (ValueError, IndexError):
            print("Selección inválida.")
            input("\nPresione Enter para continuar...")
            return

        tickets_activos_origen = [t for t in origen.tickets if t.estado != "Cancelado"]
        if destino.asientos_libres < len(tickets_activos_origen):
            print("El vuelo destino no tiene asientos suficientes para reasignar a todos los pasajeros.")
            input("\nPresione Enter para continuar...")
            return

        causa = input("Ingrese la causa de la cancelación del vuelo: ")
        fecha_canc = Utiles.controlar_fecha(input("Ingrese la fecha de cancelación (DD/MM/AAAA): "))
        origen.causa_cancelacion = causa
        origen.fecha_cancelacion = fecha_canc
        origen.estado_vuelo = "Cancelado"

        for t in origen.tripulantes:
            if all(t.documentoId != d.documentoId for d in destino.tripulantes):
                destino.tripulantes.append(t)

        def siguiente_asiento(dest):
            ocupados = {tt.numero_asiento for tt in dest.tickets if tt.estado != "Cancelado" and tt.numero_asiento is not None}
            for n in range(1, dest.capacidad_total + 1):
                if n not in ocupados:
                    return n
            return None

        a_mover = list(tickets_activos_origen)
        for t in a_mover:
            t.estado = "Cancelado"
            
            from entidades.ticket import Ticket
            nuevo_asiento = siguiente_asiento(destino)
            nuevo_ticket = Ticket(
                id_ticket=Utiles().generar_id_unico(),
                cliente=t.cliente,
                estado="Activo",
                vuelo=destino,
                numero_asiento=nuevo_asiento
            )
            destino.tickets.append(nuevo_ticket)
            
            for e in list(origen.equipajes):
                if e.pasajero.documentoId == t.cliente.documentoId:
                    if e in origen.equipajes:
                        origen.equipajes.remove(e)
                    e.vuelo = destino
                    
                    if nuevo_asiento is not None:
                        e.codigo_equipaje = f"{destino.id_vuelo}-{nuevo_asiento}"
                    destino.equipajes.append(e)

        print(
            f"El vuelo {origen.id_vuelo} ha sido cancelado y todos los pasajeros y equipajes fueron reasignados al vuelo {destino.id_vuelo}."
        )
        input("\nPresione Enter para continuar...")