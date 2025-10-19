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

    def crear_ticket():
        id_ticket = input("Ingrese el ID del ticket: ")
        cliente = input("Ingrese el nombre del cliente: ")
        estado = input("Ingrese el estado del ticket: ")
        vuelo = input("Ingrese el vuelo asociado: ")
        return f"Ticket(ID: {id_ticket}, Cliente: {cliente}, Estado: {estado}, Vuelo: {vuelo})"
    
