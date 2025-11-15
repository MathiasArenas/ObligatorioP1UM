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
        return (f"Ticket ID: {self.id_ticket} - "
                f"Cliente: {self.cliente.nombre} {self.cliente.apellido}, "
                f"Estado: {self.estado}, "
                f"Vuelo ID: {self.vuelo.id_vuelo}, "
                f"Asiento: {self.numero_asiento}")

    def crear_ticket(lista_clientes, vuelo):
   
        if int(vuelo.asientos_libres) <= 0:
            print("No hay asientos disponibles en este vuelo.")
            input("Presione Enter para continuar...")
            return None

        clientes_disponibles = []
        for cliente in lista_clientes:
            if not any(ticket.cliente.documentoId == cliente.documentoId and ticket.estado != "Cancelado" for ticket in vuelo.tickets):
                clientes_disponibles.append(cliente)

        if not clientes_disponibles:
            print("No hay clientes disponibles para asignar a este vuelo.")
            return None

        print("\nClientes disponibles para asignar:")
        for idx, cliente in enumerate(clientes_disponibles):
            print(f"{idx + 1}. {cliente.nombre} {cliente.apellido} - {cliente.documentoId}")

        try:
            seleccion = int(input("Seleccione el número del cliente: "))
            cliente = clientes_disponibles[seleccion - 1]
        except (ValueError, IndexError):
            print("Selección inválida.")
            return None

        id_ticket = Utiles().generar_id_unico()
        estado = "Activo"

        ocupados = {t.numero_asiento for t in vuelo.tickets if t.estado != "Cancelado" and t.numero_asiento is not None}
        numero_asiento = None
        for n in range(1, int(vuelo.capacidad_total) + 1):
            if n not in ocupados:
                numero_asiento = n
                break
        if numero_asiento is None:
            print("No hay asientos disponibles.")
            input("Presione Enter para continuar...")
            return None

        ticket = Ticket(
            id_ticket=id_ticket,
            cliente=cliente,
            estado=estado,
            vuelo=vuelo,
            numero_asiento=numero_asiento
        )

        vuelo.clientes.append(cliente)
        if getattr(cliente, 'fecha_ingreso_sistema', None) in (None, "", 0):
            from datetime import datetime
            cliente.fecha_ingreso_sistema = datetime.now().strftime("%d/%m/%Y")
        cliente.historial_vuelos.append(vuelo)
        vuelo.tickets.append(ticket)

        print(f"Ticket creado exitosamente para {cliente.nombre} en vuelo {vuelo.id_vuelo}.")
        print(f"Ticket: {ticket}")
        input("Presione Enter para continuar...")
        return ticket

    @staticmethod
    def cancelar_ticket(vuelo, id_cliente, id_ticket):
        if not vuelo.tickets:
            raise exc.TicketNoEncontradoError("El vuelo seleccionado no tiene tickets registrados.")

        for ticket in vuelo.tickets:
            if (
                ticket.estado != "Cancelado"
                and ticket.id_ticket.upper() == id_ticket.upper()
                and ticket.cliente.documentoId.upper() == id_cliente.upper()
            ):
                ticket.estado = "Cancelado"
                for e in vuelo.equipajes:
                    if e.pasajero.documentoId.upper() == id_cliente.upper():
                        vuelo.equipajes.remove(e)
                        break
                return ticket

        raise exc.TicketNoEncontradoError("Ticket no encontrado o ya cancelado.")


    @staticmethod
    def buscar_cliente_en_vuelo(vuelo, id_cliente):
        for ticket in vuelo.tickets:
            if ticket.estado != "Cancelado" and ticket.cliente.documentoId.upper() == id_cliente.upper():
                return ticket.cliente
            
        raise exc.ClienteNoEncontradoError(f"El cliente {id_cliente} no existe en vuelo {vuelo.id_vuelo}.")
    
    @staticmethod
    def mostrar_ticket_para_seleccion_y_cancelar(vuelo):
        Utiles.cls()
        print("Seleccione un ticket:\n")

        tickets_validos = [
            v for v in vuelo.tickets
            if v.estado != "Cancelado"
        ]

        if not tickets_validos:
            print("No hay tickets disponibles.")
            return None

        for index, ticket in enumerate(tickets_validos, start=1):
            print(f"{index}. {ticket.cliente.nombre} {ticket.cliente.apellido} | Documento: {ticket.cliente.documentoId} | Email: {ticket.cliente.email}")

        while True:
            seleccion = input("\nIngrese el número del ticket: ")

            if not seleccion.isdigit():
                print("Debe ingresar un número.")
                continue

            seleccion = int(seleccion)

            if 1 <= seleccion <= len(tickets_validos):
                ticket = tickets_validos[seleccion - 1]
                ticket.estado = "Cancelado"
                for e in list(vuelo.equipajes):
                    if e.pasajero.documentoId == ticket.cliente.documentoId:
                        vuelo.equipajes.remove(e)
                return ticket
            else:
                print("Número fuera de rango. Intente nuevamente.")