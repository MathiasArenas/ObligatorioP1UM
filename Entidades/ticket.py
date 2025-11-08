from entidades.vuelos import Vuelos
from sistema import Sistema

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
    def cancelar_ticket():
        ticket_cancelado = None
        vuelo = Vuelos.buscar_vuelo_por_id(Sistema.lista_vuelos)
        id_ticket = input("Ingrese ticket a cancelar: ")

        for ticket in vuelo.__clientes:
            if ticket.__id_ticket.upper() == id_ticket.upper():
                ticket.__estado = "Cancelado"
                print("Ticket cancelado con exito.")
                ticket_cancelado = ticket
                return ticket_cancelado
            
        Ticket.agregar_en_tickets_cancelados(ticket_cancelado)

    @staticmethod      
    def agregar_en_tickets_cancelados(ticket_cancelado):
        Sistema.lista_tickets_cancelados.append(ticket_cancelado)
