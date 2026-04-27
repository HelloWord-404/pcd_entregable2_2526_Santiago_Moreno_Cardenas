from busqueda_Aleatoria import BusquedaAleatoria
from recomendador import Recomendador
from session_Actual import Session_Actual

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estrategia = BusquedaAleatoria()
        self.recomendador = Recomendador.obtener_instancia(self, self.estrategia )
        self.cancion_actual = None

    def cargar_cancion_actual(self, id, fecha, hora):
        self.cancion_actual = Session_Actual(id, fecha, hora)

    def escuchar(self, cancion):
        if self.cancion_actual:
            self.cancion_actual.agregar_cancion_escuchada(cancion)

    def cambiar_estrategica(self, nueva):
        self.estrategia = nueva
        self.recomendador.estrategia = nueva