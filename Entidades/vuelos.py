from compania import Compania  # Cambiamos la importación

class Vuelos:
    def __init__(self, origen,destino,duracion,fecha,compania,capacidad,tipo_vuelo,id_vuelo,estado_vuelo):
        self.__origen = origen
        self.__destino = destino
        self.__duracion = duracion
        self.__fecha = fecha
        self.__compania = Compania().validar_compania(compania)
        self.__capacidad = capacidad
        self.__tipo_vuelo = tipo_vuelo
        self.__id_vuelo = id_vuelo
        self.__estado_vuelo = estado_vuelo

    @property
    def origen(self):    
        return self.__origen
    @origen.setter
    def origen(self, origen): 
        self.__origen = origen
    
    @property
    def destino(self):
        return self.__destino
    @destino.setter
    def destino(self, destino): 
        self.__destino = destino
    
    @property
    def duracion(self):
        return self.__duracion
    @duracion.setter
    def duracion(self, duracion): 
        self.__duracion = duracion
    
    @property
    def fecha(self):
        return self.__fecha
    @fecha.setter
    def fecha(self, fecha): 
        self.__fecha = fecha   
    @property
    def compania(self):
        return self.__compania
    @compania.setter
    def compania(self, compania): 
        self.__compania = Compania().validar_compania(compania)

    @property
    def capacidad(self):
        return self.__capacidad
    @capacidad.setter
    def capacidad(self, capacidad): 
        self.__capacidad = capacidad
    
    @property
    def tipo_vuelo(self):
        return self.__tipo_vuelo
    @tipo_vuelo.setter
    def tipo_vuelo(self, tipo_vuelo):
        self.__tipo_vuelo = tipo_vuelo

    @property
    def id_vuelo(self):
        return self.__id_vuelo
    @id_vuelo.setter
    def id_vuelo(self, id_vuelo):
        self.__id_vuelo = id_vuelo

    @property
    def estado_vuelo(self):
        return self.__estado_vuelo
    @estado_vuelo.setter
    def estado_vuelo(self, estado_vuelo):
        self.__estado_vuelo = estado_vuelo

       
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