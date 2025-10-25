from entidades.vuelos import Vuelos

class VuelosLogica:
    
    def registrar_vuelo():
        origen = input("Ingrese el origen del vuelo: ")
        destino = input("Ingrese el destino del vuelo: ")
        duracion = input("Ingrese la duración del vuelo: ")
        fecha = input("Ingrese la fecha del vuelo (DD/MM/AAAA): ")
        compania = input("Ingrese la compañía del vuelo: ")
        capacidad = input("Ingrese la capacidad del vuelo: ")
        tipo_vuelo = input("Ingrese el tipo de vuelo (Nacional/Internacional): ")
        id_vuelo = input("Ingrese el ID del vuelo: ")
        estado_vuelo = input("Ingrese el estado del vuelo (Activo/Cancelado): ")
        return ("Vuelo registrado", origen, destino, duracion, fecha, compania,capacidad,tipo_vuelo,id_vuelo,estado_vuelo)
    
    def validar_tipo_vuelo(tipo_vuelo):
        tipos_validos = ['Nacional', 'Internacional']
        if tipo_vuelo in tipos_validos:
            return tipo_vuelo
        else:
            raise ValueError(f"Tipo de vuelo inválido. Los tipos válidos son: {', '.join(tipos_validos)}")