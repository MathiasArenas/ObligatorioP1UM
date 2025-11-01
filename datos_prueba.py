from entidades.tripulante import Tripulante
from entidades.vuelos import Vuelos

class DatosPrueba:
         # Vuelos para pruebas
    vuelo1 = Vuelos(
        origen="Montevideo",
        destino="Buenos Aires",
        duracion=1.0,
        fecha="2025-11-15",
        compania="Aerolíneas Argentinas",
        capacidad=180,
        tipo_vuelo="Internacional",
        id_vuelo="AR123",
        estado_vuelo="Programado"
    )

    vuelo2 = Vuelos(
        origen="Madrid",
        destino="Barcelona",
        duracion=1.2,
        fecha="2025-12-01",
        compania="Iberia",
        capacidad=150,
        tipo_vuelo="Doméstico",
        id_vuelo="IB456",
        estado_vuelo="Confirmado"
    )

    # Ejemplo de tripulante
    tripulante1 = Tripulante(
        nombre="Lucía",
        apellido="Fernández",
        documentoId="UYT123456",
        email="lucia.fernandez@aviacion.com",
        celular="+59891234567",
        rol="Copiloto",
        fecha_ingreso="2022-03-10",
        horas_vuelo=850
    )
    lista_vuelos = []
    lista_clientes = []