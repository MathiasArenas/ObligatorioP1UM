from entidades.vuelos import Vuelos
from utiles import Utiles

class VuelosLogica:

    @staticmethod
    def registrar_vuelo(lista_companias):
        origen = input("Ingrese el origen del vuelo: ")
        destino = input("Ingrese el destino del vuelo: ")
        duracion = input("Ingrese la duración del vuelo (en horas): ")
        fecha = input("Ingrese la fecha del vuelo (DD/MM/AAAA): ")

        print("\nCompañías disponibles:")
        for idx, comp in enumerate(lista_companias):
            print(f"{idx + 1}. {comp.nombre} ({comp.codigo})") 

        seleccion = input("Seleccione el número de la compañía: ")
        try:
            seleccion = int(seleccion)
            compania = lista_companias[seleccion - 1]
        except (ValueError, IndexError):
            raise ValueError("Selección inválida de compañía.")

        capacidad = input("Ingrese la capacidad del vuelo: ")
        tipo_vuelo = input("Ingrese el tipo de vuelo (Nacional/Internacional): ")
        id_vuelo = Utiles().generar_id_unico()
        estado_vuelo = "Activo"

        tipo_vuelo = VuelosLogica.validar_tipo_vuelo(tipo_vuelo)

        vuelo = Vuelos(
            origen=origen,
            destino=destino,
            duracion=duracion,
            fecha=fecha,
            compania=compania,
            capacidad=capacidad,
            tipo_vuelo=tipo_vuelo,
            id_vuelo=id_vuelo,
            estado_vuelo=estado_vuelo
        )

        print(f"\nVuelo {id_vuelo} registrado correctamente.")
        return vuelo

    @staticmethod
    def validar_tipo_vuelo(tipo_vuelo):
        tipos_validos = ['Nacional', 'Internacional']
        if tipo_vuelo in tipos_validos:
            return tipo_vuelo
        else:
            raise ValueError(f"Tipo de vuelo inválido. Los tipos válidos son: {', '.join(tipos_validos)}")
        
    @staticmethod
    def cancelar_vuelo(vuelo):
        # primero tengo que validar si puedo reasignar a otro vuelo personal, pasajeros y equipajes, y si puedo cancelar debo tener una causa y fecha
        causa_cancelacion = input("Ingrese la causa de la cancelación del vuelo: ")
        fecha_cancelacion = input("Ingrese la fecha de cancelación (DD/MM/AAAA): ")
        vuelo.estado_vuelo = "Cancelado"
        print(f"El vuelo {vuelo.id_vuelo} ha sido cancelado por la siguiente causa: {causa_cancelacion} en la fecha {fecha_cancelacion}.")
    
    @staticmethod
    def mostrar_vuelo(vuelo):
        Utiles.cls()
        print("\nInformación del vuelo:")
        print(f"ID: {vuelo.id_vuelo}")
        print(f"Origen: {vuelo.origen}")
        print(f"Destino: {vuelo.destino}")
        print(f"Duración: {vuelo.duracion} horas")
        print(f"Fecha: {vuelo.fecha}")
        print(f"Compañía: {vuelo.compania.nombre} ({vuelo.compania.codigo})")
        print(f"Capacidad: {vuelo.capacidad} pasajeros")
        print(f"Tipo de vuelo: {vuelo.tipo_vuelo}")
        print(f"Estado: {vuelo.estado_vuelo}")
        input("\nPresione Enter para continuar...")
