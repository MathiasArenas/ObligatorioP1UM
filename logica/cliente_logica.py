from entidades.cliente import Cliente

class ClienteLogica:
    def registrar_persona():
        nombre = input ("Ingrese el nombre del cliente: ")
        apellido = input ("Ingrese el apellido del cliente: ")
        documentoId = input ("Ingrese el documento de identidad del cliente: ")
        email = input ("Ingrese el email del cliente: ")
        celular = input ("Ingrese el celular del cliente: ")
        nacionalidad = input ("Ingrese la nacionalidad del cliente: ")
        #historial_vuelos = input ("Ingrese el historial de vuelos del cliente: ")
        cliente = Cliente(nombre, apellido, documentoId, email, celular, nacionalidad,[])
        cliente.registrar_persona()
        return ("Cliente registrado", cliente)