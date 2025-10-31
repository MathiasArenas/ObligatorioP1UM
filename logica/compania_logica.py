from entidades.compania import Compania as Compania
from utiles import Utiles

class CompaniaLogica:
    @staticmethod

    def validar_compania(self, compania): 
        if compania in CompaniaLogica.lista_companias:
            return compania   
        else:
            raise ValueError(f"Compania '{compania}' no es válido. Debe ser uno de {CompaniaLogica.lista_companias}") # revisar luego

    def registrar_compania():
        nombre = input("Ingrese el nombre de la compañia: ")
        pais = input("Ingrese el país de la compañia: ")
        codigo = Utiles().generar_id_unico()
        compania = Compania(nombre, pais, codigo)
        return compania