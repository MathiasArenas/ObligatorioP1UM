import os

class Utiles:
    def __init__(self):
        pass

    @staticmethod
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')

    def controlar_numero(self, entrada):
        while True:
            try:
                valor = int(entrada)
                if valor < 0:
                    raise ValueError("El número debe ser positivo.")
                return valor
            except ValueError:
                entrada = input("Entrada inválida. Por favor, ingrese un número: ")

    @staticmethod
    def controlar_string(entrada):
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
    
    def generar_id_unico(self, longitud=8):
        import uuid
        return str(uuid.uuid4())[:longitud]
