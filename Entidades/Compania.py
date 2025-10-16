class Compania:
    lista_companias = ["pluna", "vali", "utl"]

    def validar_compania(self, compania):  #  ahora recibe el parámetro
        if compania in Compania.lista_companias:
            return compania   # devuelve el compania válido
        else:
            raise ValueError(f"Compania '{compania}' no es válido. Debe ser uno de {Compania.lista_companias}") # revisar luego

        