import os

class Sistema:
    @staticmethod
    def bienvenida():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("*** Bienvenido al sistema ***\n")

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

if __name__ == "__main__":
    Sistema.menu()
