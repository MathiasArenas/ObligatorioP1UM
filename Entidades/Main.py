from Cliente import Cliente
from Tripulante import Tripulante
from Vuelos import Vuelos
from Sistema import Sistema as Sis

if __name__ == "__main__":
    # cliente1=Cliente("Juan", "Perez", "12345678", "mathias@mail","099882299", "Uruguayo", ["Vuelo1", "Vuelo2"])
    # tripulante1=Tripulante("Ana", "Gomez", "87654321", "ana@mail","098877766", "Piloto", "2020-01-15", 1500)
    # vuelo1=Vuelos("Montevideo", "Buenos Aires", 1.5, "2024-07-01", "pluna")
    # print(cliente1.registrar_persona())
    # print(tripulante1.registrar_persona())
    # print(vuelo1.registrar_vuelo())
    Sis().menu()