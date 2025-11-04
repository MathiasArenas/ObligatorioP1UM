from entidades.ticket import Ticket
from entidades.vuelos import Vuelos
from utiles import Utiles

class TicketLogica:
    @staticmethod
    def crear_ticket(lista_clientes, lista_vuelos):
        vuelo = Vuelos.buscar_vuelo_por_id(lista_vuelos)
        if not vuelo:
            print("Vuelo no encontrado.")
            return None
        if int(vuelo.capacidad) <= 0:
            print("No hay asientos disponibles en este vuelo.")
            return None

        
        # Filtrar clientes no asignados al vuelo
        clientes_disponibles = [c for c in lista_clientes if c not in vuelo.clientes]

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

        # Asignar cliente al vuelo
        vuelo.clientes.append(cliente)

        # Reducir capacidad
        vuelo.capacidad = int(vuelo.capacidad) - 1

        print(f"Ticket creado exitosamente para {cliente.nombre} en vuelo {vuelo.id_vuelo}.")
        print(f"ID Ticket: {id_ticket}")
        return ticket
