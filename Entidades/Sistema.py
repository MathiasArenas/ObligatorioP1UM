import os
from utiles import Utiles
from persona import Persona
from cliente import Cliente
from tripulante import Tripulante

class Sistema:
    @staticmethod
    def bienvenida():        
        print("*** Bienvenido al sistema ***")

    @staticmethod    
    def salir():
        print("Gracias por usar el sistema. ¡Hasta luego!")

    @staticmethod
    def menu():
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
                sub_opcion = Sistema.pedir_opcion()
                match sub_opcion:
                    case 1: # Registrar Cliente
                        cliente = Cliente().registrar_persona() 
                    case 2: # Registrar Tripulante
                        tripulante = Tripulante().registrar_persona()
                    case 0:
                        Sistema.menu()
                    case _:
                        print("Opción no válida")
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10:
                pass
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
    
