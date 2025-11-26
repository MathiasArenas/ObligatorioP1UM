from utiles import Utiles
from excepciones.excepciones import Excepciones

class Compania:
    # Constructor: inicializa los atributos de una compañía
    def __init__(self,nombre, pais, codigo):
        self.__nombre = nombre
        self.__pais = pais
        self.__codigo = codigo
    
    # Getter y setter
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
    
    
    # Valida que una compañía exista dentro de la lista estática lista_companias   
    def validar_compania(self, compania): 
        if compania in Compania.lista_companias:# Se compara con una lista estatica que esta en sistemas.
            return compania   
        else:
            # Si no existe, lanza un error indicando las opciones válidas
            raise ValueError(f"Compania '{compania}' no es válido. Debe ser uno de {Compania.lista_companias}")

    # Registra una nueva compañía tomando datos del usuario
    def registrar_compania(lista_companias):
        nombre = Utiles.controlar_string (input("Ingrese el nombre de la compañia: "))
        pais = Utiles.controlar_string (input("Ingrese el país de la compañia: "))
        # Generación automática del código de compañía (formato COMP001, COMP002, etc.)
        codigo = f"COMP{len(lista_companias) + 1:03d}"
        
        # Se verifica que no exista ya una compañía con ese código
        for comp in lista_companias:
            if comp.codigo == codigo:
                raise Excepciones.DatoDuplicadoError(f"La compañía con código {codigo} ya existe.")
          
         # Se crea y retorna la nueva compañía  
        compania = Compania(nombre, pais, codigo)
        return compania
    
    # Representación en formato string de la compañía (lo que se imprime)
    def __str__(self):
        return (f"\nCompañía: {self.nombre} "
                f"\nPaís: {self.pais} \nCódigo: {self.codigo}")

    # Muestra en pantalla los datos de la compañía creada
    def mostrar_compania(self):
        print("\nCompania registrado exitosamente:")
        print(self)
        input("\nPresione Enter para continuar...")