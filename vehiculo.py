class Vehiculo:
    def __init__(self, patente: str, anio: int):
        self.patente: str = patente
        self.anio: int = anio
        self.__en_taller: bool = False

    def ingresar(self) -> str:
        if self.__en_taller:
            return "el vehiculo ya esta aki"
        self.__en_taller = True
        return "vehiculo ha ingreso al taller"

    def entregar(self) -> str:
        if not self.__en_taller:
            return "el vehiculo no se esta aki"
        self.__en_taller = False
        return "el vehiculo ha sidop entregao"
    def tarifa_hora(self) -> int:
        return 5000
    