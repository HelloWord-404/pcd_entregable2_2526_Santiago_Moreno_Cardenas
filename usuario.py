from busqueda_Aleatoria import BusquedaAleatoria
from cancion_nueva  import Cancion_Nueva
from recomendador import Recomendador
from session_Actual import Session_Actual
from cancion_nueva import Cancion_Nueva
from datetime import datetime


class Usuario:

    def __init__(self, nombre):
        self.nombre = nombre
        self.estrategia = BusquedaAleatoria()
        self.recomendador = Recomendador.obtener_instancia(self, self.estrategia )
        self.sesion_actual = Session_Actual()

    def cargar_cancion_actual(self, cancion, fecha, hora):
        cancion_nueva = Cancion_Nueva(cancion, fecha, hora)
        self.sesion_actual.agregar_cancion_escuchada(cancion_nueva)

    #def escuchar(self, cancion):
     #   self.sesion_actual.agregar_cancion_escuchada(cancion_nueva)
        

    def cambiar_estrategica(self, nueva):
        self.estrategia = nueva
        self.recomendador.estrategia = nueva