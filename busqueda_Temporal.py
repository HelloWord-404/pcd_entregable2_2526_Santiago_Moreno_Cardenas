from estrategia import Estrategia
 
class Busqueda_Temporal(Estrategia):

    def buscar(self, lista, top_n=5):

        def obtener_fecha(x):

            if hasattr(x, "fechaNacimiento"):
                return x.fechaNacimiento

            return x.fechaCreacion

        lista_ordenada = sorted(
            lista,
            key=obtener_fecha,
            reverse=True
        )

        return lista_ordenada[:top_n]