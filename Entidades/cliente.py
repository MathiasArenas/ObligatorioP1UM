from entidades.persona import Persona
from utiles import Utiles

class Cliente(Persona):
    def __init__(self, nombre, apellido, documentoId, email, celular,nacionalidad,historial_vuelos=None, fecha_ingreso_sistema=None):
        super().__init__(nombre, apellido, documentoId, email, celular)
        self.__nacionalidad = nacionalidad
        self.__historial_vuelos = historial_vuelos if None else []
        self.__fecha_ingreso_sistema = fecha_ingreso_sistema
        
    @property
    def nacionalidad(self): 
        return self.__nacionalidad
    @nacionalidad.setter
    def nacionalidad(self, nacionalidad): 
        self.__nacionalidad = nacionalidad
            
    @property
    def historial_vuelos(self): 
        return self.__historial_vuelos
    @historial_vuelos.setter
    def historial_vuelos(self, historial_vuelos):
        self.__historial_vuelos = historial_vuelos

    @property
    def fecha_ingreso_sistema(self): 
        return self.__fecha_ingreso_sistema
    
    @fecha_ingreso_sistema.setter
    def fecha_ingreso_sistema(self, fecha_ingreso_sistema):
        self.__fecha_ingreso_sistema = fecha_ingreso_sistema

    def registrar_persona():
        nombre = Utiles.controlar_string (input ("Ingrese el nombre del cliente: "))
        apellido = Utiles.controlar_string (input ("Ingrese el apellido del cliente: "))
        documentoId = Utiles.controlar_numero (input ("Ingrese el documento de identidad del cliente: "))
        email = Utiles.controlar_email (input ("Ingrese el email del cliente: "))
        celular = Utiles.controlar_numero (input ("Ingrese el celular del cliente: "))
        nacionalidad = Utiles.controlar_string (input ("Ingrese la nacionalidad del cliente: "))
        cliente = Cliente(nombre, apellido, documentoId, email, celular, nacionalidad,[])
        
        return (cliente)
    
    def __str__(self):
        return super().__str__() + f",\nNacionalidad: {self.nacionalidad}"

    def mostrar_cliente(self):
        Utiles.cls()
        print("\nCliente registrado exitosamente:")
        print(self)
        input("\nPresione Enter para continuar...")
