from estrategia import Estrategia

class Busqueda_Alfabetica(Estrategia):

    def buscar(self, lista, top_n=5):

        def obtener_nombre(x):

            if hasattr(x, "titulo"):
                return x.titulo

            return x.nombre

        lista_ordenada = sorted(
            lista,
            key=obtener_nombre
        )

        return lista_ordenada[:top_n]