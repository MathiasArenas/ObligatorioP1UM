from utiles import Utiles
from excepciones.excepciones import Excepciones

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
        
    def validar_compania(self, compania): 
        if compania in Compania.lista_companias:
            return compania   
        else:
            raise ValueError(f"Compania '{compania}' no es válido. Debe ser uno de {Compania.lista_companias}")

    def registrar_compania(lista_companias):
        nombre = Utiles.controlar_string (input("Ingrese el nombre de la compañia: "))
        pais = Utiles.controlar_string (input("Ingrese el país de la compañia: "))
        codigo = f"COMP{len(lista_companias) + 1:03d}"
        
        for comp in lista_companias:
            if comp.codigo == codigo:
                raise Excepciones.DatoDuplicadoError(f"La compañía con código {codigo} ya existe.")
            
        compania = Compania(nombre, pais, codigo)
        return compania
    
    def __str__(self):
        return (f"\nCompañía: {self.nombre} "
                f"\nPaís: {self.pais} \nCódigo: {self.codigo}")

    def mostrar_compania(self):
        print("\nCompania registrado exitosamente:")
        print(self)
        input("\nPresione Enter para continuar...")