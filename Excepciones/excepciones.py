class Excepciones:

    class ValidacionError(Exception):
        """Clase base para excepciones de validación"""
        def __init__(self, mensaje="Error de validación"):
            super().__init__(mensaje)

    class EmailInvalidoError(ValidacionError):
        """Excepción para email inválido"""
        def __init__(self, mensaje="El email debe contener '@' y '.com'"):
            super().__init__(mensaje)

    class StringVacioError(ValidacionError):
        """Excepción para strings vacíos"""
        def __init__(self, mensaje="El campo no puede estar vacío"):
            super().__init__(mensaje)

    class NumeroInvalidoError(ValidacionError):
        """Excepción para números inválidos"""
        def __init__(self, mensaje="El número debe ser positivo"):
            super().__init__(mensaje)

    class FechaInvalidaError(ValidacionError):
        """Excepción para fechas inválidas"""
        def __init__(self, mensaje="La fecha no tiene el formato correcto (AAAA-MM-DD)"):
            super().__init__(mensaje)

    class DatoDuplicadoError(ValidacionError):
        """Excepción para datos duplicados"""
        def __init__(self, mensaje="El dato ya existe en el sistema"):
            super().__init__(mensaje)

    class CapacidadExcedidaError(ValidacionError):
        """Excepción para cuando se excede la capacidad"""
        def __init__(self, mensaje="Se ha excedido la capacidad permitida"):
            self.mensaje = mensaje
            super().__init__(self.mensaje)

    class AsignacionError(ValidacionError):
        """Excepción para errores de asignación"""
        def __init__(self, mensaje="Error en la asignación"):
            super().__init__(mensaje)

    class ObjetoNoEncontradoError(Exception):
        pass

    class VueloNoEncontradoError(ObjetoNoEncontradoError):
        def __init__(self, mensaje="Vuelo no encontrado"):
            super().__init__(mensaje)

    class ClienteNoEncontradoError(ObjetoNoEncontradoError):
        def __init__(self, mensaje="Cliente no encontrado"):
            super().__init__(mensaje)

    class TicketNoEncontradoError(ObjetoNoEncontradoError):
        def __init__(self, mensaje="Tikcet no encontrado"):
            super().__init__(mensaje)
           
    class TripulanteYaAsignadoError(DatoDuplicadoError):
        def __init__(self, mensaje="El tripulante ya está asignado a este vuelo"):
            super().__init__(mensaje)