from estrategia import Estrategia

class Busqueda_Temporal(Estrategia):

    def buscar(self, lista):

        return sorted(
            lista,
            key=lambda x: x.fecha,
            reverse=True
        )[:5]