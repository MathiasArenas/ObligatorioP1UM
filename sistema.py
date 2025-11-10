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
from excepciones.excepciones import Excepciones as exc

class Sistema:
    
    cliente1 = Cliente(
        nombre="Juan",
        apellido="Pérez",
        documentoId="12345678",
        email="juan.perez@email.com",
        celular="099123456",
        nacionalidad="Uruguayo"
    )
    cliente2 = Cliente(
        nombre="María",
        apellido="González",
        documentoId="87654321",
        email="maria.gonzalez@email.com",
        celular="098765432",
        nacionalidad="Argentina"
    )
    cliente3 = Cliente(
        nombre="Carlos",
        apellido="Rodríguez",
        documentoId="11223344",
        email="carlos.rodriguez@email.com",
        celular="097111222",
        nacionalidad="Brasileño"
    )

    tripulante1 = Tripulante(
        nombre="Ana",
        apellido="López",
        documentoId="55667788",
        email="ana.lopez@airline.com",
        celular="096333444",
        rol="Piloto",
        fecha_ingreso="2010-01-15",
        horas_vuelo=5000
    )
    tripulante2 = Tripulante(
        nombre="Pedro",
        apellido="Martínez",
        documentoId="99887766",
        email="pedro.martinez@airline.com",
        celular="095555666",
        rol="Azafata",
        fecha_ingreso="2015-03-20",
        horas_vuelo=2500
    )

    compania1 = Compania(
        nombre="Sky Airlines",
        pais="Uruguay",
        codigo="AIRLINE001"
    )
    compania2 = Compania(
        nombre="Blue Wings",
        pais="Argentina",
        codigo="AIRLINE002"
    )

    ticket_V1 = Ticket(
        id_ticket="TCKT001",
        cliente=cliente1,
        vuelo="FL001",
        estado="Activo"
    )

    vuelo1 = Vuelos(
        origen="Montevideo",
        destino="Buenos Aires",
        duracion=3.25,
        fecha="2024-06-15 10:30",
        compania=compania1,
        capacidad=150,
        tipo_vuelo="Internacional",
        id_vuelo="FL001",
        estado_vuelo="Programado",
        tickets = []
    )
    vuelo1.agregar_ticket(ticket_V1)
    vuelo2 = Vuelos(
        origen="Buenos Aires",
        destino="São Paulo",
        duracion=2.5,
        fecha="2024-06-16 14:20",
        compania=compania2,
        capacidad=180,
        tipo_vuelo="Internacional",
        id_vuelo="FL002",
        estado_vuelo="Confirmado",
        tickets=[]
    )    

    lista_clientes = []
    lista_tripulantes = []
    lista_companias = []
    lista_vuelos = []
    lista_tickets_cancelados = []

    lista_clientes.extend([cliente1, cliente2, cliente3])
    lista_tripulantes.extend([tripulante1, tripulante2])
    lista_companias.extend([compania1, compania2])
    lista_vuelos.extend([vuelo1, vuelo2])

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
                if vuelo is None:
                    # Si no se pudo crear el vuelo (por ejemplo, no hay compañías), volver al menú principal
                    return
                Sistema.lista_vuelos.append(vuelo)
                VuelosLogica.mostrar_vuelo(vuelo)
            case 4:
                Utiles.cls()
                #ticket = TicketLogica.crear_ticket()
                ticket = TicketLogica.crear_ticket(Sistema.lista_clientes, Sistema.lista_vuelos)
                if ticket:
                    Sistema.lista_tickets.append(ticket)
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
                try:
                    if not Sistema.lista_vuelos:
                        raise exc.ObjetoNoEncontradoError("No hay vuelos registrados.")

                    Vuelos.mostrar_lista_vuelos(Sistema.lista_vuelos)
                    id_vuelo = input("Ingrese el ID del vuelo: ")
                    vuelo = Vuelos.buscar_vuelo_por_id(Sistema.lista_vuelos, id_vuelo)

                    id_cliente = input("Ingrese el ID del cliente para cancelar ticket: ")
                    Ticket.buscar_cliente_en_vuelo(vuelo, id_cliente)

                    id_ticket = input("Ingrese ID del ticket: ")
                    ticket = Ticket.cancelar_ticket(vuelo, id_cliente, id_ticket)
                    Sistema.lista_tickets_cancelados.append(ticket)

                    print(f"Ticket cancelado")
                    input("\nPresione Enter para continuar...")

                except exc.VueloNoEncontradoError as e:
                    print(f"{e}")
                except exc.ClienteNoEncontradoError as e:
                    print(f"{e}")
                except exc.TicketNoEncontradoError as e:
                    print(f"{e}")
                finally:
                    input("\nPresione Enter para continuar...")

            case 9:
                Utiles.cls()
                Vuelos.cancelar_vuelo(Sistema.lista_vuelos)
            case 10:
                Utiles.cls()
                Sistema.menu_informes()
                opcion_informe = Sistema.pedir_opcion()
                match opcion_informe:
                    case 1:
                        Utiles.cls()
                        Vuelos.informe_pasajeros_por_vuelo(Sistema.lista_vuelos)
                    case 2:
                        Utiles.cls()
                        Vuelos.informe_personal_asignado(Sistema.lista_vuelos)
                    case 3:
                        Utiles.cls()
                        Vuelos.informe_vuelos_por_compania(Sistema.lista_vuelos)
                    case 4:
                        Utiles.cls()
                        Vuelos.informe_vuelos_cancelados(Sistema.lista_vuelos)
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


