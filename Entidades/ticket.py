from entidades.vuelos import Vuelos
from utiles import Utiles
from excepciones.excepciones import Excepciones as exc

class Ticket:
    def __init__(self, id_ticket, cliente, estado, vuelo):
        self.__id_ticket = id_ticket
        self.__cliente = cliente
        self.__estado = estado
        self.__vuelo = vuelo

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

    def __str__(self):
        return (f"Ticket ID: {self.id_ticket} - "
                f"Cliente: {self.cliente.nombre} {self.cliente.apellido}, "
                f"Estado: {self.estado}, "
                f"Vuelo ID: {self.vuelo.id_vuelo}")

    def crear_ticket(lista_clientes, vuelo):
   
        if int(vuelo.capacidad) <= 0:
            print("No hay asientos disponibles en este vuelo.")
            return None

        clientes_disponibles = []
        for cliente in lista_clientes:            
            if not any(ticket.cliente.documentoId == cliente.documentoId for ticket in vuelo.tickets):
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

        ticket = Ticket(
            id_ticket=id_ticket,
            cliente=cliente,
            estado=estado,
            vuelo=vuelo
        )

        vuelo.clientes.append(cliente)
        # agregar historial al cliente
        cliente.historial_vuelos.append(vuelo)
        vuelo.capacidad = int(vuelo.capacidad) - 1
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
                Ticket.quitar_ticket_de_vuelo(vuelo, ticket)
                return ticket

        raise exc.TicketNoEncontradoError("Ticket no encontrado o ya cancelado.")

    @staticmethod
    def quitar_ticket_de_vuelo(vuelo, ticket):
        if ticket in vuelo.tickets:
            vuelo.tickets.remove(ticket)

    @staticmethod
    def buscar_cliente_en_vuelo(vuelo, id_cliente):
        for ticket in vuelo.tickets:
            if ticket.cliente.documentoId.upper() == id_cliente.upper():
                return ticket.cliente
            
        raise exc.ClienteNoEncontradoError(f"El cliente {id_cliente} no existe en vuelo {vuelo.id_vuelo}.")