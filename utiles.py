import os 
import re

class Utiles:
    @staticmethod
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def controlar_numero(entrada):
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
            
    @staticmethod
    def controlar_fecha(entrada):
        from datetime import datetime
        formato_fecha = "%d/%m/%Y"
        while True:
            try:
                fecha = datetime.strptime(entrada, formato_fecha)
                return fecha.strftime(formato_fecha)
            except ValueError:
                entrada = input(f"Fecha inválida. Por favor, ingrese una fecha en el formato {formato_fecha}: ")
    
    @staticmethod
    def controlar_email(entrada):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        while True:
            if re.match(patron, entrada):
                return entrada
            else:
                entrada = input("Email inválido. Ingrese un email válido (ej: ejemplo@correo.com): ")

    @staticmethod
    def obtener_fecha_actual():
        from datetime import datetime
        return datetime.now().strftime("%d/%m/%Y")