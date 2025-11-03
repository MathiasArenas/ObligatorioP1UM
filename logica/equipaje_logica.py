from entidades.equipaje import Equipaje
from entidades.vuelos import Vuelos 
from entidades.ticket import Ticket 



#class EquipajeLogica:

#    def registrar_equipaje(self):
#        equipaje = Equipaje()
#        equipaje.registrar_equipaje()
#        return ("Equipaje registrado", equipaje.peso_en_kg, equipaje.pasajero, equipaje.vuelo, equipaje.costo)

class EquipajeLogica:

    def registrar_equipaje(self, codigo_equipaje, peso_en_kg, pasajero, vuelo, costo):
        equipaje = Equipaje(codigo_equipaje, peso_en_kg, pasajero, vuelo, costo)
        equipaje.registrar_equipaje()
        return ("Equipaje registrado", equipaje.peso_en_kg, equipaje.pasajero, equipaje.vuelo, equipaje.costo)


    def registrar_equipaje(lista_vuelos, lista_tickets):
        Vuelos.mostrar_lista_vuelos(lista_vuelos)
        # id_vuelo = input("Ingrese el ID del vuelo: ")
        vuelo = Vuelos.buscar_vuelo_por_id(lista_vuelos)

        if not vuelo:
            print("Vuelo no encontrado.")
            input("\nPresione Enter para continuar...")
            return None

        id_ticket = input("Ingrese el número de ticket: ")
        ticket = next((t for t in lista_tickets if t.id_ticket == id_ticket and t.vuelo.id_vuelo == vuelo.id_vuelo), None)

        if not ticket or not ticket.cliente:
            print("Ticket inválido o sin cliente asignado.")
            input("\nPresione Enter para continuar...")
            return None

        try:
            peso = float(input("Ingrese el peso del equipaje en kg: "))
        except ValueError:
            print("Peso inválido.")
            return None

        if peso > 45:
            print("No se admite equipaje mayor a 45kg.")
            input("\nPresione Enter para continuar...")
            return None

        tipo = vuelo.tipo_vuelo.lower()
        costo = 0

        if peso <= 23:
            costo = 0
        elif 24 <= peso <= 32:
            costo = 100 if tipo == "internacional" else 30
        elif 33 <= peso <= 45:
            costo = 200 if tipo == "internacional" else 60

        
        codigo_equipaje = f"{vuelo.id_vuelo}-{ticket.id_ticket}"

        equipaje = Equipaje(
            codigo_equipaje=codigo_equipaje,
            peso_en_kg=peso,
            pasajero=ticket.cliente,
            vuelo=vuelo,
            costo=costo
        )

        vuelo.equipajes.append(equipaje)

        print("\nEquipaje registrado exitosamente:")
        print(equipaje)
        input("\nPresione Enter para continuar...")
        return equipaje