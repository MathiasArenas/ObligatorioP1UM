from entidades.compania import Compania as CompaniaEntidad

class CompaniaLogica:

    def validar_compania(self, compania): 
        if compania in CompaniaLogica.lista_companias:
            return compania   
        else:
            raise ValueError(f"Compania '{compania}' no es válido. Debe ser uno de {CompaniaLogica.lista_companias}") # revisar luego

    def registrar_compania():
        nombre = input("Ingrese el nombre de la compañia: ")
        pais = input("Ingrese el país de la compañia: ")
        codigo = input("Ingrese el código de la compañia: ")
        nueva_compania = CompaniaEntidad(nombre, pais, codigo)
        nueva_compania.registrar_compania()
        return ("Compañia registrada", nueva_compania)
