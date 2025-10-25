from entidades.tripulante import Tripulante

class TripulanteLogica:
    
    def registrar_persona():
        nombre = input ("Ingrese el nombre del tripulante: ")
        apellido = input ("Ingrese el apellido del tripulante: ")
        documentoId = input ("Ingrese el documento de identidad del tripulante: ")
        email = input ("Ingrese el email del tripulante: ")
        celular = input ("Ingrese el celular del tripulante: ")
        rol = input ("Ingrese el rol del tripulante (Piloto, Copiloto, Azafata): ")
        fecha_ingreso = input ("Ingrese la fecha de ingreso del tripulante (DD/MM/AAAA): ")
        #horas_vuelo = input ("Ingrese las horas de vuelo del tripulante: ") 
        tripulante = Tripulante (nombre, apellido, documentoId, email, celular, rol, fecha_ingreso,[]) 
        tripulante.registrar_persona()
        return ("Tripulante registrado", tripulante)
        
    def asignar_personal_vuelo():
        #print("Asignar personal a vuelo")
        id_vuelo = input("Ingrese el ID del vuelo: ")
        rol = input("Ingrese el rol del tripulante (Piloto, Copiloto, Azafata): ")
        nombre = input("Ingrese el nombre del tripulante: ")
        apellido = input("Ingrese el apellido del tripulante: ")
        estado_vuelo = input("Ingrese el estado del vuelo (Activo/Cancelado): ")
        
         # Crear un diccionario con la asignación
        asignacion = {
            "id_vuelo": id_vuelo,
            "rol": rol,
            "nombre": nombre,
            "apellido": apellido,
            "estado_vuelo": estado_vuelo
        }
        
        return asignacion