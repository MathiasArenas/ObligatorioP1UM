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

    def registrar_compania(self):
        pass
    
    def __str__(self):
        return (f"\nCompañía: {self.nombre} "
                f"\nPaís: {self.pais} \nCódigo: {self.codigo}")

    def mostrar_compania(self):
        print("\nCompania registrado exitosamente:")
        print(self)
        input("\nPresione Enter para continuar...")