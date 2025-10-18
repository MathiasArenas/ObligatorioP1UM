class Utiles:
    def __init__(self):
        pass

    def controlar_numero(self, entrada):
        while True:
            try:
                valor = int(entrada)
                return valor
            except ValueError:
                entrada = input("Entrada inválida. Por favor, ingrese un número: ")

    def controlar_srting(self, entrada):
        while True:
            if entrada.strip() == "":
                entrada = input("Entrada inválida. Por favor, ingrese un texto válido: ")
            else:
                return entrada
    
    def controlar_fecha(self, entrada):
        from datetime import datetime
        formato_fecha = "%Y-%m-%d"
        while True:
            try:
                fecha = datetime.strptime(entrada, formato_fecha)
                return fecha.strftime(formato_fecha)
            except ValueError:
                entrada = input(f"Fecha inválida. Por favor, ingrese una fecha en el formato {formato_fecha}: ")
