from excepciones.excepciones import Excepciones

class Equipaje:
    # Constructor: inicializa un equipaje con todos sus datos
    def __init__(self, codigo_equipaje, peso_en_kg, pasajero, vuelo, costo):
        self.__codigo_equipaje = codigo_equipaje
        self.__peso_en_kg = peso_en_kg
        self.__pasajero = pasajero
        self.__vuelo = vuelo
        self.__costo = costo

    # Getter y setter
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
        
    # Representación del equipaje en formato string
    def __str__(self):
        return (f"Equipaje {self.codigo_equipaje} - "
            f"Pasajero: {self.pasajero.nombre} {self.pasajero.apellido}, "
            f"Peso: {self.peso_en_kg}kg, Costo: USD {self.costo}")

    
    # Método estático encargado de registrar equipaje para un vuelo
    @staticmethod
    def registrar_equipaje(vuelo):
        ex = Excepciones() # Instancia para usar excepciones personalizadas
         
         # Obtener los tickets activos del vuelo(que no esten cancelados)
        tickets_activos = [t for t in vuelo.tickets if t.estado != "Cancelado"]
              
        if not tickets_activos:
            print("No hay tickets activos para este vuelo.")
            input("\nPresione Enter para continuar...")
            return None

        print("\n--- Tickets activos del vuelo ---")

        # Mostrar tickets con más información
        for i, t in enumerate(tickets_activos, 1):
            print(
                f"{i}. {t.id_ticket} - {t.cliente.nombre} {t.cliente.apellido},"
                f"Estado: {t.estado},"
                f" Asiento: {getattr(t, 'numero_asiento', 'No asignado')},"
                f" Vuelo: {t.vuelo.id_vuelo} ({t.vuelo.origen} -> {t.vuelo.destino})"
            )

        # Selección del ticket
        try:
            indice = int(input("\nSeleccione el ticket por número: "))
            ticket = tickets_activos[indice - 1]
        except (ValueError, IndexError):
            print("Selección inválida.")
            input("\nPresione Enter para continuar...")
            return None
        # Validaciones del ticket seleccionado
        try:
            if not ticket:
                raise Excepciones.TicketNoEncontradoError("El ticket no existe o no pertenece al vuelo.")

            if not ticket.cliente:
                raise Excepciones.AsignacionError("El ticket no tiene un pasajero asignado.")
        except Exception as e:
            print(f"\nError: {e}")
            input("\nPresione Enter para continuar...")
            return None

        # Solicita el peso del equipaje
        try:
            peso = float(input("Ingrese el peso del equipaje en kg: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            return None
        
        # Valida el límite máximo permitido
        try:
            if peso > 45:
                raise Excepciones.CapacidadExcedidaError("El equipaje no puede superar los 45 kg.")
        except Exception as e:
            print(f"\nError: {e}")
            input("\nPresione Enter para continuar...")
            return None
        
        # Revisa si el pasajero ya registró equipaje previamente
        try:
            if any(e.pasajero.documentoId == ticket.cliente.documentoId for e in vuelo.equipajes):
                raise Excepciones.DatoDuplicadoError("Este pasajero ya tiene un equipaje registrado.")
        except Exception as e:
            print(f"\nError: {e}")
            input("\nPresione Enter para continuar...")
            return None

        # Cálculo del costo en función del peso y tipo de vuelo
        tipo = vuelo.tipo_vuelo.lower()
        costo = 0

        if peso <= 23:
            costo = 0
        elif 24 <= peso <= 32:
            costo = 100 if tipo == "internacional" else 30
        elif 33 <= peso <= 45:
            costo = 200 if tipo == "internacional" else 60

        # El código del equipaje se forma con el ID del vuelo y asiento (o ID de ticket si no hay)
        codigo_equipaje = f"{vuelo.id_vuelo}-{ticket.numero_asiento if getattr(ticket, 'numero_asiento', None) is not None else ticket.id_ticket}"

        # Se crea la instancia de Equipaje
        equipaje = Equipaje(
            codigo_equipaje=codigo_equipaje,
            peso_en_kg=peso,
            pasajero=ticket.cliente,
            vuelo=vuelo,
            costo=costo
        )

        # Se agrega el equipaje al vuelo
        vuelo.equipajes.append(equipaje)

        print("\nEquipaje registrado exitosamente:")
        print(equipaje)
        input("\nPresione Enter para continuar...")