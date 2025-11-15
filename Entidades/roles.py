class Roles:
    lista_roles = ["Piloto", "Copiloto", "Azafata"]

    def validar_rol(self, rol):
        if not isinstance(rol, str):
            raise ValueError("El rol debe ser un texto.")

        mapa = {
            "piloto": "Piloto",
            "copiloto": "Copiloto",
            "azafata": "Azafata",
        }
        clave = rol.strip().lower()
        if clave in mapa:
            return mapa[clave]
        else:
            raise ValueError(f"Rol '{rol}' no es válido. Debe ser uno de {Roles.lista_roles}")
    
    def mostrar_roles(self):
        return Roles.lista_roles
    
