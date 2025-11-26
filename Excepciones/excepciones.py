class Excepciones:

    # Excepción base para todos los errores de validación
    class ValidacionError(Exception):
        """Clase base para excepciones de validación"""
        def __init__(self, mensaje="Error de validación"):
            super().__init__(mensaje)

    # Error cuando un email no cumple el formato esperado
    class EmailInvalidoError(ValidacionError):
        """Excepción para email inválido"""
        def __init__(self, mensaje="El email debe contener '@' y '.com'"):
            super().__init__(mensaje)

    # Error cuando un string viene vacío o solo espacios
    class StringVacioError(ValidacionError):
        """Excepción para strings vacíos"""
        def __init__(self, mensaje="El campo no puede estar vacío"):
            super().__init__(mensaje)

    # Error cuando se espera un número válido pero no lo es
    class NumeroInvalidoError(ValidacionError):
        """Excepción para números inválidos"""
        def __init__(self, mensaje="El número debe ser positivo"):
            super().__init__(mensaje)

    # Error cuando la fecha ingresada no cumple el formato correcto
    class FechaInvalidaError(ValidacionError):
        """Excepción para fechas inválidas"""
        def __init__(self, mensaje="La fecha no tiene el formato correcto (DD/MM/AA)"):
            super().__init__(mensaje)

    # Error cuando un dato ya está registrado en el sistema
    class DatoDuplicadoError(ValidacionError):
        """Excepción para datos duplicados"""
        def __init__(self, mensaje="El dato ya existe en el sistema"):
            super().__init__(mensaje)

    # Error cuando se supera la capacidad permitida (ej: asientos)
    class CapacidadExcedidaError(ValidacionError):
        """Excepción para cuando se excede la capacidad"""
        def __init__(self, mensaje="Se ha excedido la capacidad permitida"):
            self.mensaje = mensaje
            super().__init__(self.mensaje)

    # Error genérico para fallos de asignación (tripulantes, clientes, etc.)
    class AsignacionError(ValidacionError):
        """Excepción para errores de asignación"""
        def __init__(self, mensaje="Error en la asignación"):
            super().__init__(mensaje)

    # Excepción base para objetos no encontrados en el sistema
    class ObjetoNoEncontradoError(Exception):
        pass

    # Error cuando un vuelo no se encuentra en la búsqueda
    class VueloNoEncontradoError(ObjetoNoEncontradoError):
        def __init__(self, mensaje="Vuelo no encontrado"):
            super().__init__(mensaje)

    # Error cuando un cliente no existe en la base de datos
    class ClienteNoEncontradoError(ObjetoNoEncontradoError):
        def __init__(self, mensaje="Cliente no encontrado"):
            super().__init__(mensaje)

    # Error cuando no se encuentra un ticket
    class TicketNoEncontradoError(ObjetoNoEncontradoError):
        def __init__(self, mensaje="Tikcet no encontrado"):
            super().__init__(mensaje)

    # Error cuando un tripulante ya está asignado al mismo vuelo
    class TripulanteYaAsignadoError(DatoDuplicadoError):
        def __init__(self, mensaje="El tripulante ya está asignado a este vuelo"):
            super().__init__(mensaje)