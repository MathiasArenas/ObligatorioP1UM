from entidades.persona import Persona
from entidades.cliente import Cliente
from entidades.tripulante import Tripulante
from entidades.vuelos import Vuelos
from entidades.compania import Compania
from entidades.ticket import Ticket
from entidades.equipaje import Equipaje
from sistema import Sistema

class DatosPrueba:
    def __init__(self):
        # Clientes
        self.cliente1 = Cliente("Juan", "Pérez", "12345678", "juan.perez@email.com", "099123456", "Uruguayo")
        self.cliente2 = Cliente("María", "González", "87654321", "maria.gonzalez@email.com", "098765432", "Argentina")
        self.cliente3 = Cliente("Carlos", "Rodríguez", "11223344", "carlos.rodriguez@email.com", "097111222", "Brasileño")
        self.cliente4 = Cliente("Lucía", "Fernández", "33445566", "lucia.fernandez@email.com", "099876543", "Chilena")
        self.cliente5 = Cliente("Diego", "Silva", "44556677", "diego.silva@email.com", "098112233", "Uruguayo")
        self.cliente6 = Cliente("Sofía", "Ramírez", "55667788", "sofia.ramirez@email.com", "097654321", "Paraguaya")
        self.cliente7 = Cliente("Andrés", "Torres", "66778899", "andres.torres@email.com", "096987654", "Colombiano")
        self.cliente8 = Cliente("Valentina", "Morales", "77889900", "valentina.morales@email.com", "095321654", "Peruana")
        self.cliente9 = Cliente("Martín", "Castro", "88990011", "martin.castro@email.com", "094456789", "Mexicano")
        self.cliente10 = Cliente("Camila", "Vega", "99001122", "camila.vega@email.com", "093789012", "Ecuatoriana")
        self.clientes = [self.cliente1, self.cliente2, self.cliente3, self.cliente4, self.cliente5,
                         self.cliente6, self.cliente7, self.cliente8, self.cliente9, self.cliente10]

        # Tripulantes
        self.tripulante1 = Tripulante("Ana", "López", "55667788", "ana.lopez@airline.com", "096333444", "Piloto", "2010-01-15", 5000)
        self.tripulante2 = Tripulante("Pedro", "Martínez", "99887766", "pedro.martinez@airline.com", "095555666", "Azafata", "2015-03-20", 2500)
        self.tripulante3 = Tripulante("Juan", "Mendez", "99887744", "juan.mendez@airline.com", "095555123", "Copiloto", "2015-03-20", 150)
        self.tripulantes = [self.tripulante1, self.tripulante2, self.tripulante3]

        # Compañías
        self.compania1 = Compania("Sky Airlines", "Uruguay", "AIRLINE001")
        self.compania2 = Compania("Blue Wings", "Argentina", "AIRLINE002")
        self.companias = [self.compania1, self.compania2]

        # Vuelos
        self.vuelo1 = Vuelos("Montevideo", "Buenos Aires", 3.25, "2024-06-15 10:30", self.compania1, 150, "Internacional", "FL001", "Programado", [])
        self.vuelo2 = Vuelos("Buenos Aires", "São Paulo", 2.5, "2024-06-16 14:20", self.compania2, 180, "Internacional", "FL002", "Confirmado", [])
        self.vuelos = [self.vuelo1, self.vuelo2]

        # Tickets
        self.ticket1 = Ticket("TCKT001", self.cliente1, self.vuelo1, "Activo")
        self.vuelo1.tickets.append(self.ticket1)
        self.tickets = [self.ticket1]
        self.tickets_cancelados = []

    def cargar_en_sistema(self, sistema: Sistema):
        sistema.lista_clientes.extend(self.clientes)
        sistema.lista_tripulantes.extend(self.tripulantes)
        sistema.lista_companias.extend(self.companias)
        sistema.lista_vuelos.extend(self.vuelos)
        sistema.lista_tickets.extend(self.tickets)
        sistema.lista_tickets_cancelados.extend(self.tickets_cancelados)