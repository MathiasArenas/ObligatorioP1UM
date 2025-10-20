from entidades.equipaje import Equipaje

class EquipajeLogica:

    def registrar_equipaje(self):
        equipaje = Equipaje()
        equipaje.registrar_equipaje()
        return ("Equipaje registrado", equipaje.peso_en_kg, equipaje.pasajero, equipaje.vuelo, equipaje.costo)
