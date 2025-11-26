# Importa herramientas para crear clases abstractas
from abc import ABC, abstractmethod

# Clase abstracta Persona: sirve como base para otras clases (Cliente, Tripulante, etc.)
class Persona(ABC):
    def __init__(self, nombre, apellido, documentoId, email, celular):
        self.__nombre = nombre
        self.__apellido = apellido        
        self.__documentoId = documentoId
        self.__email = email
        self.__celular = celular
        
    #getters y setters
    
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
        
    # Método abstracto: obliga a las clases hijas a implementar su propia forma de registrar personas
    @abstractmethod
    def registrar_persona(self):
        pass

    # Representación en formato string de la persona (lo que se imprime)
    def __str__(self):
        return (
            f"\nNombre: {self.nombre},"
            f"\nApellido: {self.apellido},"
            f"\nDocumento: {self.documentoId},"
            f"\nEmail: {self.email},"
            f"\nCelular: {self.celular}"
            )    
    
    def mostrar_persona(self):
        print(self)





