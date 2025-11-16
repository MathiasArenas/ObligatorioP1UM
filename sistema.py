from utiles import Utiles
from entidades.cliente import Cliente
from entidades.tripulante import Tripulante
from entidades.vuelos import Vuelos
from entidades.compania import Compania
from entidades.ticket import Ticket
from excepciones.excepciones import Excepciones as exc
from entidades.equipaje import Equipaje

class Sistema:

    lista_clientes = []
    lista_tripulantes = []
    lista_companias = []
    lista_vuelos = []
    lista_tickets_cancelados = []

    # Clientes
    cliente1 = Cliente("Juan", "Pérez", "12345678", "juan.perez@email.com", "099123456", "Uruguayo")
    cliente2 = Cliente("María", "González", "87654321", "maria.gonzalez@email.com", "098765432", "Argentina")
    cliente3 = Cliente("Carlos", "Rodríguez", "11223344", "carlos.rodriguez@email.com", "097111222", "Brasileño")
    cliente4 = Cliente("Lucía", "Fernández", "33445566", "lucia.fernandez@email.com", "099876543", "Chilena")
    cliente5 = Cliente("Diego", "Silva", "44556677", "diego.silva@email.com", "098112233", "Uruguayo")
    cliente6 = Cliente("Sofía", "Ramírez", "55667788", "sofia.ramirez@email.com", "097654321", "Paraguaya")
    cliente7 = Cliente("Andrés", "Torres", "66778899", "andres.torres@email.com", "096987654", "Colombiano")
    cliente8 = Cliente("Valentina", "Morales", "77889900", "valentina.morales@email.com", "095321654", "Peruana")
    cliente9 = Cliente("Martín", "Castro", "88990011", "martin.castro@email.com", "094456789", "Mexicano")
    cliente10 = Cliente("Camila", "Vega", "99001122", "camila.vega@email.com", "093789012", "Ecuatoriana")   

    # Tripulantes
    tripulante1 = Tripulante("Ana", "López", "55667788", "ana.lopez@airline.com", "096333444", "Piloto", "2010-01-15", 5000)
    tripulante2 = Tripulante("Pedro", "Martínez", "99887766", "pedro.martinez@airline.com", "095555666", "Azafata", "2015-03-20", 2500)
    tripulante3 = Tripulante("Juan", "Mendez", "99887744", "juan.mendez@airline.com", "095555123", "Copiloto", "2015-03-20", 150)
    tripulante4 = Tripulante("Laura", "Gómez", "11224433", "laura.gomez@airline.com", "094444555", "Azafata", "2018-07-10", 1200)
    tripulante5 = Tripulante("Esteban", "Ruiz", "22334455", "esteban.ruiz@airline.com", "093333222", "Piloto", "2008-05-01", 6200)
    tripulante6 = Tripulante("Natalia", "Cabrera", "33445566", "natalia.cabrera@airline.com", "092222111", "Copiloto", "2012-11-30", 3100)
    tripulante7 = Tripulante("Gustavo", "Pereyra", "44556677", "gustavo.pereyra@airline.com", "091111000", "Azafata", "2016-04-18", 1800)
    tripulante8 = Tripulante("Mónica", "Sosa", "55667799", "monica.sosa@airline.com", "090000999", "Azafata", "2019-09-25", 950)
    tripulante9 = Tripulante("Ricardo", "Alonso", "66778800", "ricardo.alonso@airline.com", "089999888", "Piloto", "2005-02-12", 7200)
    tripulante10 = Tripulante("Carla", "Ferrer", "77889911", "carla.ferrer@airline.com", "088888777", "Copiloto", "2013-06-05", 2700)

    # Compañías
    compania1 = Compania("Sky Airlines", "Uruguay", "AIRLINE001")
    compania2 = Compania("Blue Wings", "Argentina", "AIRLINE002")
    compania3 = Compania("Andes Jet", "Chile", "AIRLINE003")
    compania4 = Compania("Tango Air", "Argentina", "AIRLINE004")
    compania5 = Compania("Sol del Sur", "Uruguay", "AIRLINE005")
    compania6 = Compania("Amazonas Fly", "Brasil", "AIRLINE006")
    compania7 = Compania("Patagonia Wings", "Chile", "AIRLINE007")
    compania8 = Compania("Altura Jet", "Perú", "AIRLINE008")
    compania9 = Compania("Pampa Air", "Argentina", "AIRLINE009")
    compania10 = Compania("AeroPacífico", "México", "AIRLINE010")

    # Vuelos
    vuelo1 = Vuelos("Montevideo", "Buenos Aires", 3.25, "2026-06-15 10:30", compania1, 5, "Internacional", "FL001", "Activo", [])
    vuelo2 = Vuelos("Buenos Aires", "São Paulo", 2.5, "2026-06-16 14:20", compania2, 2, "Internacional", "FL002", "Activo", [])
    vuelo3 = Vuelos("Santiago", "Lima", 3.0, "2026-06-17 09:00", compania3, 3, "Internacional", "FL003", "Activo", [])
    vuelo4 = Vuelos("Montevideo", "Asunción", 2.0, "2026-06-18 11:45", compania5, 4, "Internacional", "FL004", "Activo", [])
    vuelo5 = Vuelos("Montevideo", "Punta del Este", 0.75, "2026-06-23 07:30", compania1, 100, "Nacional", "FL005", "Activo", [])

    # Tickets
    ticket_v1_1 = Ticket("TCKT_v1_1", cliente1, "Activo", vuelo1, numero_asiento=1)
    vuelo1.tickets.append(ticket_v1_1)
    vuelo1.tripulantes.extend([tripulante1, tripulante2, tripulante3])

    ticket_v1_2 = Ticket("TCKT_v1_2", cliente6, "Activo", vuelo1, numero_asiento=2)
    vuelo1.tickets.append(ticket_v1_2)

    ticket_v1_3 = Ticket("TCKT_v1_3", cliente7, "Activo", vuelo1, numero_asiento=3)
    vuelo1.tickets.append(ticket_v1_3)

    ticket_v1_4 = Ticket("TCKT_v1_4", cliente5, "Activo", vuelo1, numero_asiento=4)
    vuelo1.tickets.append(ticket_v1_4)

    ticket_v2_1 = Ticket("TCKT_v2_1", cliente2, "Activo", vuelo2, numero_asiento=1)
    vuelo2.tickets.append(ticket_v2_1)

    ticket_v2_2 = Ticket("TCKT_v2_2", cliente8, "Activo", vuelo2, numero_asiento=2)
    vuelo2.tickets.append(ticket_v2_2)

    ticket_v2_3 = Ticket("TCKT_v2_3", cliente9, "Activo", vuelo2, numero_asiento=3)
    vuelo2.tickets.append(ticket_v2_3)

    ticket_v3 = Ticket("TCKT_v3_1", cliente3, "Activo", vuelo3, numero_asiento=1)
    vuelo3.tickets.append(ticket_v3)

    ticket_v3_2 = Ticket("TCKT_v3_2", cliente10, "Activo", vuelo3, numero_asiento=2)
    vuelo3.tickets.append(ticket_v3_2)

    ticket_v4_1 = Ticket("TCKT_v4_1", cliente4, "Activo", vuelo4, numero_asiento=1)
    vuelo4.tickets.append(ticket_v4_1)

    lista_clientes.extend([cliente1, cliente2, cliente3, cliente4, cliente5, cliente6, cliente7, cliente8, cliente9, cliente10])
    lista_tripulantes.extend([tripulante1, tripulante2, tripulante3, tripulante4, tripulante5, tripulante6, tripulante7, tripulante8, tripulante9, tripulante10])
    lista_companias.extend([compania1, compania2, compania3, compania4, compania5, compania6, compania7, compania8, compania9, compania10])
    lista_vuelos.extend([vuelo1, vuelo2, vuelo3, vuelo4, vuelo5])

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
        print('2. Copiloto')
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
                        try:
                            cliente = Cliente.registrar_persona(Sistema.lista_clientes)
                            Sistema.lista_clientes.append(cliente)                        
                            cliente.mostrar_cliente()
                        except exc.DatoDuplicadoError as e:
                            print(f"{e}")
                            input("\nPresione Enter para continuar...")
                    case 2: # Registrar Tripulante
                        Utiles.cls()
                        tripulante = Tripulante.registrar_persona()
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
                compania =Compania.registrar_compania()
                Sistema.lista_companias.append(compania)
                compania.mostrar_compania()
            case 3:
                Utiles.cls()
                vuelo = Vuelos.registrar_vuelo(Sistema.lista_companias)
                if vuelo is None:
                    
                    return
                Sistema.lista_vuelos.append(vuelo)
                Vuelos.mostrar_vuelo(vuelo)
            case 4:
                Utiles.cls()
                vuelo = Vuelos.mostrar_vuelo_para_seleccion(Sistema.lista_vuelos)

                if vuelo is None:
                    print("Selección inválida.")
                    input("Enter para continuar...")
                    return

                Ticket.crear_ticket(Sistema.lista_clientes, vuelo)

            case 5:
                Utiles.cls()
                try:
                    vuelo = Vuelos.mostrar_vuelo_para_seleccion(Sistema.lista_vuelos)
                    Vuelos.asignar_personal_vuelo(Sistema.lista_tripulantes,vuelo)    
                
                except exc.VueloNoEncontradoError as e:
                    print(f"{e}")
                except exc.TripulanteYaAsignadoError as e:
                    print(f"{e}")
                finally:
                    input("\nPresione Enter para continuar...")
                            
            case 6:
                Utiles.cls()
                vuelo = Vuelos.mostrar_vuelo_para_seleccion(Sistema.lista_vuelos)
                Equipaje.registrar_equipaje(vuelo)
                vuelo.listar_equipajes_por_vuelo()

            case 7:
                Utiles.cls()
                Vuelos.visualizar_vuelos(Sistema.lista_vuelos)

            case 8:
                Utiles.cls()
                try:

                    vuelo = Vuelos.mostrar_vuelo_para_seleccion(Sistema.lista_vuelos)
                    ticket = Ticket.mostrar_ticket_para_seleccion_y_cancelar(vuelo)
                        
                    Sistema.lista_tickets_cancelados.append(ticket)

                    print(f"Ticket cancelado")

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