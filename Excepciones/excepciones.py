class ValidacionError(Exception):
    """Clase base para excepciones de validación"""
    pass

class EmailInvalidoError(ValidacionError):
    """Excepción para email inválido"""
    def __init__(self, mensaje="El email debe contener '@' y '.com'"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class StringVacioError(ValidacionError):
    """Excepción para strings vacíos"""
    def __init__(self, mensaje="El campo no puede estar vacío"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class NumeroInvalidoError(ValidacionError):
    """Excepción para números inválidos"""
    def __init__(self, mensaje="El número debe ser positivo"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class FechaInvalidaError(ValidacionError):
    """Excepción para fechas inválidas"""
    def __init__(self, mensaje="La fecha no tiene el formato correcto (AAAA-MM-DD)"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class DatoDuplicadoError(ValidacionError):
    """Excepción para datos duplicados"""
    def __init__(self, mensaje="El dato ya existe en el sistema"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class CapacidadExcedidaError(ValidacionError):
    """Excepción para cuando se excede la capacidad"""
    def __init__(self, mensaje="Se ha excedido la capacidad permitida"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class AsignacionError(ValidacionError):
    """Excepción para errores de asignación"""
    def __init__(self, mensaje="Error en la asignación"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class objetoNoEncontradoError(ValidacionError):
    """Excepción para cuando un objeto no es encontrado"""
    def __init__(self, mensaje="El objeto no fue encontrado"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
        