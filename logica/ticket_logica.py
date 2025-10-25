from entidades.ticket import Ticket

class TicketLogica:
    
    def crear_ticket():
        id_ticket = input("Ingrese el ID del ticket: ")
        cliente = input("Ingrese el nombre del cliente: ")
        estado = input("Ingrese el estado del ticket: ")
        vuelo = input("Ingrese el vuelo asociado: ")
        return f"Ticket(ID: {id_ticket}, Cliente: {cliente}, Estado: {estado}, Vuelo: {vuelo})"
    
