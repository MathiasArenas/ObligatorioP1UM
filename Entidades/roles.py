class Roles:
    lista_roles = ["piloto", "copiloto", "azafata"]

    def validar_rol(self, rol):  #  ahora recibe el parámetro
        if rol.lower() in Roles.lista_roles:
            return rol   # devuelve el rol válido
        else:
            raise ValueError(f"Rol '{rol}' no es válido. Debe ser uno de {Roles.lista_roles}") # revisar luego
    
    def mostrar_roles(self):
        return Roles.lista_roles
    
