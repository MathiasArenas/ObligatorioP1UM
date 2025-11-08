from entidades.vuelos import Vuelos
from utiles import Utiles

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
        if value not in ("Activo", "Cancelado"):
            raise ValueError("Estado debe ser 'Activo' o 'Cancelado'.")
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
    def cancelar_ticket(lista_vuelos, lista_tickets_cancelados):
        Utiles.cls()
        vuelo = Vuelos.buscar_vuelo_por_id(lista_vuelos)
        id_ticket = input("Ingrese ticket a cancelar: ")

        for ticket in vuelo.tickets:
            if ticket.id_ticket.upper() == id_ticket.upper():
                ticket.estado = "Cancelado"
                Ticket.agregar_en_tickets_cancelados(ticket, lista_tickets_cancelados)
                Ticket.quitar_ticket_de_vuelo(vuelo, ticket)                
                print("Ticket cancelado con exito.")
                return
            
        input("\nPresione Enter para continuar...")
        return

    @staticmethod      
    def agregar_en_tickets_cancelados(ticket_cancelado, lista_tickets_cancelados):
        lista_tickets_cancelados.append(ticket_cancelado)

    @staticmethod
    def quitar_ticket_de_vuelo(vuelo, ticket):
        if ticket in vuelo.tickets:
            vuelo.tickets.remove(ticket)
