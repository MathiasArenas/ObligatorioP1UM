import os
from utiles import Utiles
from persona import Persona
from cliente import Cliente
from tripulante import Tripulante
from vuelos import Vuelos
from compania import Compania
from ticket import Ticket

class Sistema:
    lista_tripulantes = []
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
                        Cliente.registrar_persona() 
                    case 2: # Registrar Tripulante
                        Tripulante.registrar_persona()
                    case 0:
                        Sistema.menu()
                    case _:
                        print("Opción no válida")
            case 2:
                Compania.registrar_compania()
            case 3:
                Vuelos.registrar_vuelo()
            case 4:
                Ticket.crear_ticket()
                pass
            case 5:
                tripulante = Tripulante.asignar_personal_vuelo()
                Sistema.lista_tripulantes.append(tripulante)
            case 6:
                Equipaje.registrar_equipaje_bodega()
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
    
