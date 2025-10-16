from abc import ABC, abstractmethod

class Persona(ABC):
    #inicializacion de constructores
    def __init__(self, nombre, apellido, documentoId, email, celular):
        self.__nombre = nombre
        self.__apellido = apellido        
        self.__documentoId = documentoId
        self.__email = email
        self.__celular = celular
        
    @property
    def nombre(self): 
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre): 
        self.__nombre = nombre
    
    @property
    def apellido(self): 
        return self.__apellido
    @apellido.setter
    def apellido(self, apellido): 
        self.__apellido = apellido
    
    @property
    def documentoId(self): 
        return self.__documentoId
    @documentoId.setter
    def documentoId(self, documentoId): 
        self.__documentoId = documentoId
    
    @property
    def email(self): 
        return self.__email
    @email.setter
    def email(self, email):
        self.__email = email
    
    @property   
    def celular(self): 
        return self.__celular
    @celular.setter
    def celular(self, celular): 
        self.__celular = celular
        
    @abstractmethod
    def registrar_persona(self):
        pass
    
class Cliente(Persona):
    def __init__(self, nombre, apellido, documentoId, email, celular,nacionalidad,historial_vuelos):
        super().__init__(nombre, apellido, documentoId, email, celular)
        self.__nacionalidad = nacionalidad
        self.__historial_vuelos = historial_vuelos
    def registrar_persona(self):
        return ("Cliente registrado", self.nombre, self.apellido, self.documentoId, self.email, self.celular, self.__nacionalidad, self.__historial_vuelos)


class Tripulante(Persona): 
    def __init__(self, nombre, apellido, documentoId, email, celular, rol, fecha_ingreso, horas_vuelo):
        super().__init__(nombre, apellido, documentoId, email, celular)
        self.__rol = Roles().validar_rol(rol)
        self.__fecha_ingreso = fecha_ingreso
        self.__horas_vuelo = horas_vuelo
    
    def registrar_persona(self):
        return ("Tripulante registrado", self.nombre, self.apellido, self.documentoId, self.email, self.celular, self.__rol, self.__fecha_ingreso, self.__horas_vuelo)
        

class Roles:
    lista_roles = ["Piloto", "Copiloto", "Azafata"]

    def validar_rol(self, rol):  #  ahora recibe el parámetro
        if rol in Roles.lista_roles:
            return rol   # devuelve el rol válido
        else:
            raise ValueError(f"Rol '{rol}' no es válido. Debe ser uno de {Roles.lista_roles}") # revisar luego
    
    def mostrar_roles(self):
        return Roles.lista_roles
    
class Compania:
    lista_companias = ["pluna", "vali", "utl"]

    def validar_compania(self, compania):  #  ahora recibe el parámetro
        if compania in Compania.lista_companias:
            return compania   # devuelve el compania válido
        else:
            raise ValueError(f"Compania '{compania}' no es válido. Debe ser uno de {Compania.lista_companias}") # revisar luego

        

class Vuelos:
    def __init__(self, origen,destino,duracion,fecha,compania):
        self.__origen = origen
        self.__destino = destino
        self.__duracion = duracion
        self.__fecha = fecha
        self.__compania = Compania().validar_compania(compania)
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
        
    def registrar_vuelo(self):
        return ("Vuelo registrado", self.__origen, self.__destino, self.__duracion, self.__fecha, self.__compania)


if __name__ == "__main__":
    cliente1=Cliente("Juan", "Perez", "12345678", "mathias@mail","099882299", "Uruguayo", ["Vuelo1", "Vuelo2"])
    tripulante1=Tripulante("Ana", "Gomez", "87654321", "ana@mail","098877766", "Piloto", "2020-01-15", 1500)
    vuelo1=Vuelos("Montevideo", "Buenos Aires", 1.5, "2024-07-01", "pluna")
    print(cliente1.registrar_persona())
    print(tripulante1.registrar_persona())
    print(vuelo1.registrar_vuelo())
    