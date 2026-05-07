from estrategia import Estrategia

class Busqueda_Alfabetica(Estrategia):

    def buscar(self, lista):

        return sorted(
            lista,
            key=lambda x: x.nombre
        )[:5]