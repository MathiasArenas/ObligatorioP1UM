import os
from entidades import equipaje
from utiles import Utiles
from entidades.persona import Persona
from entidades.cliente import Cliente
from entidades.tripulante import Tripulante
from entidades.vuelos import Vuelos
from entidades.compania import Compania
from entidades.ticket import Ticket
from logica.cliente_logica import ClienteLogica
from logica.tripulante_logica import TripulanteLogica
from logica.vuelos_logica import VuelosLogica
from logica.compania_logica import CompaniaLogica
from logica.equipaje_logica import EquipajeLogica
from logica.ticket_logica import TicketLogica
from datos_prueba import DatosPrueba as dp

class Sistema:
    
    lista_tripulantes = []
    lista_clientes = []
    lista_companias = []
    lista_vuelos = []
    lista_tickets = []
    lista_equipajes = []
    vuelo: Vuelos = None

    lista_vuelos.extend([dp.vuelo1, dp.vuelo2])
    lista_tripulantes.append(dp.tripulante1)

    
    @staticmethod
    def bienvenida():        
        print("*** Bienvenido al sistema ***")

    @staticmethod    
    def salir():
        print("Gracias por usar el sistema. ¡Hasta luego!")

    @staticmethod
    def menu():
        Utiles.cls()
        Sistema.bienvenida()
        print('1. Registrar Persona')
        print('2. Registrar Compañia')
        print('3. Crear Vuelo')
        print('4. Crear ticket')
        print('5. Asignar personal a vuelos')
        print('6. Registrar equipaje en bodega')
        print('7. Visualizar vuelos')
        print('8. Cancelar ticket')
        print('9. Cancelar vuelo')
        print('10. Informes a emitir')
        print('0. Salir\n')

    @staticmethod
    def menu_persona():
        print('1. Registrar Cliente')
        print('2. Registrar Tripulante')
        print('0. Volver al menú principal\n')

    @staticmethod    
    def menu_tripulante():
        print('1. Piloto')
        print('2. Copilito')
        print('3. Azafata')
        print('0. Volver al menú principal\n')

    @staticmethod    
    def menu_informes():
        print('1. Informe de pasajeros por vuelo')
        print('2. Informe de personal asignado')
        print('3. Informe de vuelos por compañía')
        print('4. Informe de vuelos cancelados')
        print('0. Volver al menú principal\n')

    def pedir_opcion():
        opcion = input("Seleccione una opción: ")
        opcion = Utiles().controlar_numero(opcion)
        Utiles.cls()

        return opcion
    
    def casos_opciones(opcion):
        match opcion:
            case 1: # Registrar Persona
                Utiles.cls()
                Sistema.menu_persona()
                opcion_persona = Sistema.pedir_opcion()
                match opcion_persona:
                    case 1: # Registrar Cliente
                        Utiles.cls()
                        cliente = ClienteLogica.registrar_persona()
                        Sistema.lista_clientes.append(cliente)                        
                        cliente.mostrar_cliente()
                    case 2: # Registrar Tripulante
                        Utiles.cls()
                        tripulante = TripulanteLogica.registrar_persona()
                        Sistema.lista_tripulantes.append(tripulante)
                        tripulante.mostrar_tripulante()
                    case 0:
                        Utiles.cls()
                        Sistema.menu()
                    case _:
                        Utiles.cls()
                        print("Opción no válida")
            case 2:
                Utiles.cls()
                compania =CompaniaLogica.registrar_compania()
                Sistema.lista_companias.append(compania)
                compania.mostrar_compania()
            case 3:
                Utiles.cls()
                vuelo = VuelosLogica.registrar_vuelo(Sistema.lista_companias)
                Sistema.lista_vuelos.append(vuelo)
                VuelosLogica.mostrar_vuelo(vuelo)
            case 4:
                Utiles.cls()
                #ticket = TicketLogica.crear_ticket()
                ticket = TicketLogica.crear_ticket(Sistema.lista_clientes, Sistema.lista_vuelos)
                Sistema.lista_tickets.append(ticket)
                pass
            case 5:
                Utiles.cls()
                Vuelos.asignar_personal_vuelo(Sistema.lista_vuelos, Sistema.lista_tripulantes)                
            case 6:
                Utiles.cls()
                equipaje = EquipajeLogica.registrar_equipaje(Sistema.lista_vuelos, Sistema.lista_tickets)
                if equipaje:
                    Sistema.lista_equipajes.append(equipaje)

            case 7:
                Utiles.cls()
                #Vuelos.visualizar_vuelos()
                Vuelos.visualizar_vuelos(Sistema.lista_vuelos)
            case 8:
                Utiles.cls()
                Ticket.cancelar_ticket()
            case 9:
                Utiles.cls()
                VuelosLogica.cancelar_vuelo(Sistema.lista_vuelos)
            case 10:
                Utiles.cls()
                Sistema.menu_informes()
                opcion_informe = Sistema.pedir_opcion()
                match opcion_informe:
                    case 1:
                        Utiles.cls()
                        # a. Informe de pasajeros por vuelo: Listado con nombre, cédula, nacionalidad y cantidad de equipaje.
                        Vuelos.informe_pasajeros_por_vuelo(Sistema.lista_vuelos)
                    case 2:
                        Utiles.cls()
                        Tripulante.informe_personal_asignado()
                    case 3:
                        Utiles.cls()
                        Vuelos.informe_vuelos_por_compania()
                    case 4:
                        Utiles.cls()
                        Vuelos.informe_vuelos_cancelados()
                    case 0:
                        Utiles.cls()
                        Sistema.menu()
                    case _:
                        Utiles.cls()
                        print("Opción no válida")
            case 0:
                Utiles.cls()
                Sistema.salir()
            case _:
                Utiles.cls()
                print("Opción no válida")
    
    def manejar_menu():
        while True:
            Sistema.menu()
            opcion = Sistema.pedir_opcion()
            if opcion == 0:
                Sistema.salir()
                break
            else:
                Sistema.casos_opciones(opcion)


