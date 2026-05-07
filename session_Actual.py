class Session_Actual:
    def __init__(self, id, fecha, hora):
        self.id = id
        self.fecha = fecha
        self.hora = hora
        self.canciones_durante_session = []  # Lista de canciones

    def agregar_cancion_escuchada(self, cancion):
        self.canciones_durante_session.append(cancion)

    def calcular_media(self):
        if not self.canciones_durante_session:
            return {}

    # unir atributos
        claves = self.canciones_durante_session[0].atributosSonoros.keys()
        claves2 = self.canciones_durante_session[0].atributosSentimentales.keys()

        media = {}

    # SONOROS
        for k in claves:
            media[k] = sum(
                c.atributosSonoros[k] for c in self.canciones_durante_session
                ) / len(self.canciones_durante_session)

    # SENTIMENTALES
        for k in claves2:
            media[k] = sum(
                c.atributosSentimentales[k] for c in self.canciones_durante_session
            ) / len(self.canciones_durante_session)

        return media