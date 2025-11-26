from entidades.persona import Persona
from excepciones.excepciones import Excepciones
#importamos funciones de utilidad validaciones, limpieza pantalla, etc
from utiles import Utiles

class Cliente(Persona):
    # Constructor: inicializa un cliente con datos personales y atributos propios
    def __init__(self, nombre, apellido, documentoId, email, celular,nacionalidad,historial_vuelos=None, fecha_ingreso_sistema=None):
         # Llama al constructor de Persona para asignar atributos heredados
        super().__init__(nombre, apellido, documentoId, email, celular)
        self.__nacionalidad = nacionalidad
        # Lista de vuelos realizados; si no se pasa, se inicializa vacía
        self.__historial_vuelos = historial_vuelos if historial_vuelos is not None else []
        self.__fecha_ingreso_sistema = fecha_ingreso_sistema
        
    # Getter para nacionalidad
    @property
    def nacionalidad(self): 
        return self.__nacionalidad
    # Setter para nacionalidad
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
    
     # Método estático para registrar un nuevo cliente interactuando con el usuario
    @staticmethod
    def registrar_persona(lista_clientes):
        nombre = Utiles.controlar_string(input("Ingrese el nombre del cliente: "))
        apellido = Utiles.controlar_string(input("Ingrese el apellido del cliente: "))
        documentoId = Utiles.controlar_numero(input("Ingrese el documento de identidad del cliente: "))

        # Se verifica que el documento no exista ya en la lista de clientes
        for c in lista_clientes:
            if c.documentoId == documentoId:
                raise Excepciones.DatoDuplicadoError(f"El cliente con documento {documentoId} ya existe.")
        
        # Se piden y validan los demás datos
        email = Utiles.controlar_email(input("Ingrese el email del cliente: "))
        celular = Utiles.controlar_numero(input("Ingrese el celular del cliente: "))
        nacionalidad = Utiles.controlar_string(input("Ingrese la nacionalidad del cliente: "))

        # Se crea un nuevo cliente
        cliente = Cliente(nombre, apellido, documentoId, email, celular, nacionalidad, [], None)
        return cliente
        
    # Representación en formato string del cliente, heredando el __str__ de Persona
    def __str__(self):
        return super().__str__() + f",\nNacionalidad: {self.nacionalidad}"

    # Muestra en pantalla la información del cliente ya registrado
    def mostrar_cliente(self):
        Utiles.cls()
        print("\nCliente registrado exitosamente:")
        print(self)
        input("\nPresione Enter para continuar...")