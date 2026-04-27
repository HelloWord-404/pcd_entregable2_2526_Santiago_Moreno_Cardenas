import random

class BusquedaAleatoria(Estrategia):
    def buscar(self, lista, funcion_match):
        while True:
            elemento = random.choice(lista)
            if funcion_match(elemento):
                return elemento