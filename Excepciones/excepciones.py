class ValidacionError(Exception):
    """Clase base para excepciones de validación"""
    pass

class EmailInvalidoError(ValidacionError):
    """Excepción para email inválido"""
    def __init__(self, mensaje="El email debe contener '@' y '.com'"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ValidacionesHelper:
    @staticmethod
    def validar_email(email):
        """Valida el formato del email"""
        if '@' not in email or '.com' not in email:
            raise EmailInvalidoError()
        return email