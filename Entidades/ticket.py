from entidades.vuelos import Vuelos
from utiles import Utiles
from excepciones.excepciones import Excepciones as exc

class Ticket:
    def __init__(self, id_ticket, cliente, estado, vuelo, numero_asiento=None):
        self.__id_ticket = id_ticket
        self.__cliente = cliente
        self.__estado = estado
        self.__vuelo = vuelo
        self.__numero_asiento = numero_asiento

    #getters y setters
    
    @property
    def id_ticket(self):
        return self.__id_ticket

    @id_ticket.setter
    def id_ticket(self, value):
        self.__id_ticket = value

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, value):
        self.__cliente = value

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, value):
        self.__estado = value

    @property
    def vuelo(self):
        return self.__vuelo

    @vuelo.setter
    def vuelo(self, value):
        # Validación para evitar asignar objetos incorrectos
        if not isinstance(value, Vuelos):
            raise TypeError("El vuelo asignado debe ser un objeto de la clase Vuelos.")
        self.__vuelo = value

    @property
    def numero_asiento(self):
        return self.__numero_asiento

    @numero_asiento.setter
    def numero_asiento(self, value):
        self.__numero_asiento = value

    def __str__(self):
        # Representación amigable del ticket
        return (f"Ticket ID: {self.id_ticket} - "
                f"Cliente: {self.cliente.nombre} {self.cliente.apellido}, "
                f"Estado: {self.estado}, "
                f"Vuelo ID: {self.vuelo.id_vuelo}, "
                f"Asiento: {self.numero_asiento}")

    def crear_ticket(lista_clientes, vuelo):
        
        # Verificar si el vuelo tiene toda la tripulación requerida
        if not vuelo.validar_tripulacion_completa():
            roles_faltantes = vuelo.obtener_roles_faltantes()
            print(f"\nADVERTENCIA: Este vuelo no tiene tripulación completa.")
            print(f"Faltan: {', '.join(roles_faltantes)}")
            #Se pregunta al usuario si quiere continuar
            confirmar = input("¿Desea crear el ticket de todos modos? (S/N): ").strip().upper()
            if confirmar != "S":
                print("Creación de ticket cancelada.")
                input("Presione Enter para continuar...")
                return None

         # Si no hay asientos, se cancela la operación
        if int(vuelo.asientos_libres) <= 0:
            print("No hay asientos disponibles en este vuelo.")
            input("Presione Enter para continuar...")
            return None

        # Lista clientes que NO tienen un ticket activo para este vuelo
        clientes_disponibles = []
        for cliente in lista_clientes:
            if not any(ticket.cliente.documentoId == cliente.documentoId and ticket.estado != "Cancelado" for ticket in vuelo.tickets):
                clientes_disponibles.append(cliente)

        # Si no hay clientes elegibles
        if not clientes_disponibles:
            print("No hay clientes disponibles para asignar a este vuelo.")
            return None

         # Mostrar clientes elegibles
        print("\nClientes disponibles para asignar:")
        for idx, cliente in enumerate(clientes_disponibles):
            print(f"{idx + 1}. {cliente.nombre} {cliente.apellido} - {cliente.documentoId}")

        # Selección segura del cliente
        try:
            seleccion = int(input("Seleccione el número del cliente: "))
            cliente = clientes_disponibles[seleccion - 1]
        except (ValueError, IndexError):
            print("Selección inválida.")
            return None

        # Generación del ID del ticket de la siguiente forma: TKT_<ID_VUELO>_<NÚMERO_SECUENCIAL>
        id_ticket = f"TKT_{vuelo.id_vuelo}_{len(vuelo.tickets) + 1:03d}"
        estado = "Activo"

        # Determinar los asientos ocupados actualmente
        ocupados = {t.numero_asiento for t in vuelo.tickets if t.estado != "Cancelado" and t.numero_asiento is not None}
        
        # Buscar el primer asiento libre disponible
        numero_asiento = None
        for n in range(1, int(vuelo.capacidad_total) + 1):
            if n not in ocupados:
                numero_asiento = n
                break
        # Si no hay asiento asignable
        if numero_asiento is None:
            print("No hay asientos disponibles.")
            input("Presione Enter para continuar...")
            return None

        # Crear el ticket final
        ticket = Ticket(
            id_ticket=id_ticket,
            cliente=cliente,
            estado=estado,
            vuelo=vuelo,
            numero_asiento=numero_asiento
        )

        # Registrar cliente en el vuelo si aún no está
        vuelo.clientes.append(cliente)
        
        # Asignar fecha de ingreso al sistema si es su primera vez
        if cliente.fecha_ingreso_sistema is None:
            from datetime import datetime
            cliente.fecha_ingreso_sistema = datetime.now().strftime("%d/%m/%Y")
        
        # Agregar vuelo al historial del cliente y ticket al vuelo
        cliente.historial_vuelos.append(vuelo)
        vuelo.tickets.append(ticket)

        print(f"Ticket creado exitosamente para {cliente.nombre} en vuelo {vuelo.id_vuelo}.")
        print(f"Ticket: {ticket}")
        input("Presione Enter para continuar...")
        return ticket
    
    @staticmethod
    def mostrar_ticket_para_seleccion_y_cancelar(vuelo):
        Utiles.cls()
        print("Seleccione un ticket:\n")

        # Filtrar solo tickets activos
        tickets_validos = [
            v for v in vuelo.tickets
            if v.estado != "Cancelado"
        ]

        if not tickets_validos:
            print("No hay tickets disponibles.")
            return None

        # Mostrar tickets para seleccionar
        for index, ticket in enumerate(tickets_validos, start=1):
            print(f"{index}. {ticket.cliente.nombre} {ticket.cliente.apellido} | Documento: {ticket.cliente.documentoId} | Email: {ticket.cliente.email}")

        # Bucle para selección segura de ticket
        while True:
            seleccion = input("\nIngrese el número del ticket: ")

            # Validación de entrada
            if not seleccion.isdigit():
                print("Debe ingresar un número.")
                continue

            seleccion = int(seleccion)

            # Validación de rango
            if 1 <= seleccion <= len(tickets_validos):
                ticket = tickets_validos[seleccion - 1]
                # Se cambia estado a cancelado
                ticket.estado = "Cancelado"
                # Se eliminan equipajes asociados al cliente
                for e in list(vuelo.equipajes):
                    if e.pasajero.documentoId == ticket.cliente.documentoId:
                        vuelo.equipajes.remove(e)
                return ticket
            else:
                print("Número fuera de rango. Intente nuevamente.")