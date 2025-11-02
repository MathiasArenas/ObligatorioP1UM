class Equipaje:
    def __init__(self, codigo_equipaje, peso_en_kg, pasajero, vuelo, costo):
        self.__codigo_equipaje = codigo_equipaje
        self.__peso_en_kg = peso_en_kg
        self.__pasajero = pasajero
        self.__vuelo = vuelo
        self.__costo = costo

    @property
    def codigo_equipaje(self):
        return self.__codigo_equipaje
    @codigo_equipaje.setter
    def codigo_equipaje(self, codigo_equipaje):
        self.__codigo_equipaje = codigo_equipaje

    @property
    def peso_en_kg(self):
        return self.__peso_en_kg
    @peso_en_kg.setter
    def peso_en_kg(self, peso_en_kg): 
        self.__peso_en_kg = peso_en_kg
    
    @property
    def pasajero(self):
        return self.__pasajero
    @pasajero.setter
    def pasajero(self, pasajero): 
        self.__pasajero = pasajero

    @property
    def vuelo(self):
        return self.__vuelo
    @vuelo.setter
    def vuelo(self, vuelo): 
        self.__vuelo = vuelo
    
    @property
    def costo(self):
        return self.__costo
    @costo.setter
    def costo(self, costo): 
        self.__costo = costo
        
    def registrar_equipaje(self):
        pass

    def __str__(self):
        return (f"Equipaje {self.codigo_equipaje} - "
            f"Pasajero: {self.pasajero.nombre} {self.pasajero.apellido}, "
            f"Peso: {self.peso_en_kg}kg, Costo: USD {self.costo}")
