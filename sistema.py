import os
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

class Sistema:
    
    lista_tripulantes = []
    lista_clientes = []
    lista_companias = []
    lista_vuelos = []
    lista_tickets = []
    lista_equipajes = []
    vuelo: Vuelos = None
   
    
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

        return opcion
    
    def casos_opciones(opcion):
        match opcion:
            case 1: # Registrar Persona
                Sistema.menu_persona()
                opcion_persona = Sistema.pedir_opcion()
                match opcion_persona:
                    case 1: # Registrar Cliente
                        cliente = ClienteLogica.registrar_persona()
                        Sistema.lista_clientes.append(cliente)                        
                        cliente.mostrar_cliente()

                    case 2: # Registrar Tripulante
                        tripulante = TripulanteLogica.registrar_persona()
                        Sistema.lista_tripulantes.append(tripulante)
                        tripulante.mostrar_tripulante()
                    case 0:
                        Sistema.menu()
                    case _:
                        print("Opción no válida")
            case 2:
                compania =CompaniaLogica.registrar_compania()
                Sistema.lista_companias.append(compania)
                compania.mostrar_compania()
            case 3:
                vuelo = VuelosLogica.registrar_vuelo(Sistema.lista_companias)
                Sistema.lista_vuelos.append(vuelo)

            case 4:
                ticket = TicketLogica.crear_ticket()
                Sistema.lista_tickets.append(ticket)
                pass
            case 5:
                tripulante = TripulanteLogica.registrar_persona()   
                VuelosLogica.registrar_vuelo(vuelo,tripulante)
            case 6:
                equipaje = EquipajeLogica.registrar_equipaje()
                Sistema.lista_equipajes.append(equipaje)
            case 7:
                Vuelos.visualizar_vuelos()
            case 8:
                Ticket.cancelar_ticket()
            case 9:
                Vuelos.cancelar_vuelo()
            case 10:
                Sistema.menu_informes()
                opcion_informe = Sistema.pedir_opcion()
                match opcion_informe:
                    case 1:
                        Ticket.informe_pasajeros_por_vuelo()
                    case 2:
                        Tripulante.informe_personal_asignado()
                    case 3:
                        Vuelos.informe_vuelos_por_compania()
                    case 4:
                        Vuelos.informe_vuelos_cancelados()
                    case 0:
                        Sistema.menu()
                    case _:
                        print("Opción no válida")
            case 0:
                Sistema.salir()
            case _:
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

