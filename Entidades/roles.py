class Roles:
    lista_roles = ["Piloto", "Copiloto", "Azafata"]

    # Método que valida que un rol ingresado sea correcto
    def validar_rol(self, rol):
        # Verifica que el valor recibido sea texto
        if not isinstance(rol, str):
            raise ValueError("El rol debe ser un texto.")
        
            # Mapea entradas en minúsculas a los roles correctos
        mapa = {
            "piloto": "Piloto",
            "copiloto": "Copiloto",
            "azafata": "Azafata",
        }
        # Limpia espacios y convierte a minúsculas para validar correctamente
        clave = rol.strip().lower()
        # Si el rol existe en el mapa, devuelve la versión correcta
        if clave in mapa:
            return mapa[clave]
        else:
            # Si no coincide con ningún rol permitido, lanza error
            raise ValueError(f"Rol '{rol}' no es válido. Debe ser uno de {Roles.lista_roles}")
    
    # Devuelve la lista de roles disponibles
    def mostrar_roles(self):
        return Roles.lista_roles
    
