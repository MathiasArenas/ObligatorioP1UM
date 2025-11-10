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
        self.__vuelo = value

    def crear_ticket(self):
        pass

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