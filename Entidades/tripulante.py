from entidades.persona import Persona
from entidades.roles import Roles
from utiles import Utiles

class Tripulante(Persona): 
    def __init__(self, nombre, apellido, documentoId, email, celular, rol, fecha_ingreso, horas_vuelo=None):
        super().__init__(nombre, apellido, documentoId, email, celular)
        self.__rol = Roles().validar_rol(rol)
        self.__fecha_ingreso = fecha_ingreso
        #self.__horas_vuelo = horas_vuelo if None else []
        
    @property
    def rol(self):
        return self.__rol
    @rol.setter
    def rol(self, rol):
        self.__rol = Roles().validar_rol(rol)
    @property
    def fecha_ingreso(self):
        return self.__fecha_ingreso
    @fecha_ingreso.setter
    def fecha_ingreso(self, fecha_ingreso):
        self.__fecha_ingreso = fecha_ingreso
    @property
    def horas_vuelo(self):
        return self.__horas_vuelo
    @horas_vuelo.setter
    def horas_vuelo(self, horas_vuelo):
        self.__horas_vuelo = horas_vuelo
    
<<<<<<< HEAD
    def registrar_persona(self):
        pass

    def __str__(self):
        return (
        super().__str__() +
        f",\nRol: {self.rol},"
        f"\nFecha de Ingreso: {self.fecha_ingreso}"
        )      

    def mostrar_tripulante(self):
        Utiles.cls()
        print("\Tripulante registrado exitosamente:")
        print(self)
        input("\nPresione Enter para continuar...")
    
=======
    
    def __str__(self):
        return (f"Tripulante: {self.nombre} {self.apellido}, "
                f"Documento: {self.documentoId}, Email: {self.email}, "
                f"Celular: {self.celular}, Rol: {self.rol}, "
                f"Fecha de Ingreso: {self.fecha_ingreso}")
        
    def mostrar_tripulante(self):
        print("\nTripulante registrado exitosamente:")
        print(self)
        input("\nPresione Enter para continuar...")    
>>>>>>> f22db57a2e9cbf653a7a6a7629674f16b567fb78
