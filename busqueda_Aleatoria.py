import random
from estrategia import Estrategia

class BusquedaAleatoria(Estrategia):

    def buscar(self, lista):

        random.shuffle(lista)

        return lista[:5]