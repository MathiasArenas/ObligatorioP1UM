class Ticket():
    def __init__(self, id_ticket, cliente, estado, vuelo):
        self.id_ticket = id_ticket
        self.cliente = cliente
        self.estado = estado
        self.vuelo = vuelo

    def __str__(self):
        return f"Ticket(ID: {self.id_ticket}, Cliente: {self.cliente}, Estado: {self.estado}, Valor: {self.vuelo})"