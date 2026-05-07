class Session_Actual:

    def __init__(self):
        self.canciones_durante_session = []  # Lista de canciones

    def agregar_cancion_escuchada(self, cancion):
        self.canciones_durante_session.append(cancion)

    class Session_Actual:

    def __init__(self):
        self.canciones_durante_session = []

    def agregar_cancion_escuchada(self, cancion):
        self.canciones_durante_session.append(cancion)

    def calcular_media(self):

        if len(self.canciones_durante_session) == 0:
            return {}
        suma = {}
        # recorremos canciones escuchadas
        for c in self.canciones_durante_session:
            atributos = c.cancion.atributosSonoros.copy()
            atributos.update(c.cancion.atributosSentimentales)
            for k in atributos: # sumar atributos
                if k not in suma:
                    suma[k] = 0
                suma[k] += atributos[k]
        # sacar promedio de todos los atributos generalos
        media = {}

        for k in suma:
            media[k] = (
                suma[k] /
                len(self.canciones_durante_session)
            )

        # buscamos 3 mayores atributos, seran los lideres, y el recomendador se basara en ellos para su busqueda
        ordenados = sorted(
            media.items(),
            key=lambda x: x[1],
            reverse=True
        )

        top3 = ordenados[:3]

        atributos_lider = []
        suma_top = 0

        for x in top3:
            atributos_lider.append(x[0])
            suma_top += x[1]

        promedio_top = suma_top / 3

        promedio_total = (
            sum(media.values()) /
            len(media)
        )

        return {
            "atributos_lider": atributos_lider,
            "promedio_top": promedio_top,
            "promedio_total": promedio_total
        }