from entidades.ticket import Ticket
from entidades.vuelos import Vuelos

class TicketLogica:
    @staticmethod
    def crear_ticket(lista_clientes, lista_vuelos):
        id_ticket = input("Ingrese el ID del ticket: ")

        documento_cliente = input("Ingrese el documento del cliente: ")
        cliente = next((c for c in lista_clientes if c.documentoId == documento_cliente), None)
        if not cliente:
            print("Cliente no encontrado.")
            return None

        estado = input("Ingrese el estado del ticket: ")

        Vuelos.mostrar_lista_vuelos(lista_vuelos)
        id_vuelo = input("Ingrese el ID del vuelo asociado: ")
        vuelo = Vuelos.buscar_vuelo_por_id(lista_vuelos)
        if not vuelo:
            print("Vuelo no encontrado.")
            return None

        ticket = Ticket(id_ticket=id_ticket, cliente=cliente, estado=estado, vuelo=vuelo)
        print(f"\nTicket creado exitosamente para {cliente.nombre} en vuelo {vuelo.id_vuelo}.")
        return ticket   


#    def crear_ticket():
#        id_ticket = input("Ingrese el ID del ticket: ")
#        cliente = input("Ingrese el nombre del cliente: ")
#        estado = input("Ingrese el estado del ticket: ")
#        vuelo = input("Ingrese el vuelo asociado: ")
#        return f"Ticket(ID: {id_ticket}, Cliente: {cliente}, Estado: {estado}, Vuelo: {vuelo})"
    
