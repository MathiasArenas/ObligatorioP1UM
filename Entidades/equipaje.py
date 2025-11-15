class Equipaje:
    def __init__(self, codigo_equipaje, peso_en_kg, pasajero, vuelo, costo):
        self.__codigo_equipaje = codigo_equipaje
        self.__peso_en_kg = peso_en_kg
        self.__pasajero = pasajero
        self.__vuelo = vuelo
        self.__costo = costo


    @property
    def codigo_equipaje(self):
        return self.__codigo_equipaje
    @codigo_equipaje.setter
    def codigo_equipaje(self, codigo_equipaje):
        self.__codigo_equipaje = codigo_equipaje


    @property
    def peso_en_kg(self):
        return self.__peso_en_kg
    @peso_en_kg.setter
    def peso_en_kg(self, peso_en_kg): 
        self.__peso_en_kg = peso_en_kg
    
    @property
    def pasajero(self):
        return self.__pasajero
    @pasajero.setter
    def pasajero(self, pasajero): 
        self.__pasajero = pasajero

    @property
    def vuelo(self):
        return self.__vuelo
    @vuelo.setter
    def vuelo(self, vuelo): 
        self.__vuelo = vuelo
    
    @property
    def costo(self):
        return self.__costo
    @costo.setter
    def costo(self, costo): 
        self.__costo = costo
        
    def __str__(self):
        return (f"Equipaje {self.codigo_equipaje} - "
            f"Pasajero: {self.pasajero.nombre} {self.pasajero.apellido}, "
            f"Peso: {self.peso_en_kg}kg, Costo: USD {self.costo}")

    

    def registrar_equipaje(vuelo):
              
        vuelo.listar_tickets_por_vuelo()   

        id_ticket = input("Ingrese el número de ticket: ")
        ticket = None
        for t in vuelo.tickets:
            if t.id_ticket == id_ticket and t.vuelo.id_vuelo == vuelo.id_vuelo and t.estado != "Cancelado":
                ticket = t
                break

        if not ticket or not ticket.cliente:
            print("Ticket inválido, cancelado o sin cliente asignado.")
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

        if any(e.pasajero.documentoId == ticket.cliente.documentoId for e in vuelo.equipajes):
            print("Este pasajero ya tiene un equipaje registrado para este vuelo.")
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

        codigo_equipaje = f"{vuelo.id_vuelo}-{ticket.numero_asiento if getattr(ticket, 'numero_asiento', None) is not None else ticket.id_ticket}"

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