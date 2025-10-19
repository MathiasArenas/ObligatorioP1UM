class Compania:
    def __init__(self,nombre, pais, codigo):
        self.__nombre = nombre
        self.__pais = pais
        self.__codigo = codigo
        
        @property
        def nombre(self):
            return self.__nombre
        @nombre.setter
        def nombre(self, nombre): 
            self.__nombre = nombre

        @property
        def pais(self): 
            return self.__pais
        @pais.setter
        def pais(self, pais): 
            self.__pais = pais

        @property
        def codigo(self):
            return self.__codigo
        @codigo.setter
        def codigo(self, codigo): 
            self.__codigo = codigo

    def validar_compania(self, compania):  #  ahora recibe el parámetro
        if compania in Compania.lista_companias:
            return compania   # devuelve el compania válido
        else:
            raise ValueError(f"Compania '{compania}' no es válido. Debe ser uno de {Compania.lista_companias}") # revisar luego

    def registrar_compania(self):
        self.__nombre = input("Ingrese el nombre de la compañia: ")
        self.__pais = input("Ingrese el país de la compañia: ")
        self.__codigo = input("Ingrese el código de la compañia: ")
        return ("Compañia registrada", self.__nombre, self.__pais, self.__codigo) 
