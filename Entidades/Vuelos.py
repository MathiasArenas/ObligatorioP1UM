from compania import Compania  # Cambiamos la importación

class Vuelos:
    def __init__(self, origen,destino,duracion,fecha,compania,capacidad):
        self.__origen = origen
        self.__destino = destino
        self.__duracion = duracion
        self.__fecha = fecha
        self.__compania = Compania().validar_compania(compania)
        self.__capacidad = capacidad
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
    def capacidad(self):
        return self.__capacidad
    @capacidad.setter
    def capacidad(self, capacidad): 
        self.__capacidad = capacidad   
        
    def registrar_vuelo(self):
        self.__origen = input("Ingrese el origen del vuelo: ")
        self.__destino = input("Ingrese el destino del vuelo: ")
        self.__duracion = input("Ingrese la duración del vuelo: ")
        self.__fecha = input("Ingrese la fecha del vuelo (DD/MM/AAAA): ")
        self.__compania = input("Ingrese la compañía del vuelo: ")
        self.__capacidad = input("Ingrese la capacidad del vuelo: ")
        return ("Vuelo registrado", self.__origen, self.__destino, self.__duracion, self.__fecha, self.__compania,self.__capacidad)

    # vuelo1=Vuelos("Montevideo", "Buenos Aires", 1.5, "2024-07-01", "pluna")
    # print(vuelo1.registrar_vuelo())