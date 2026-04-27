class Recomendador:
    _instancias = {}  # guarda recomendadores por usuario

    @classmethod
    def obtener_instancia(cls, usuario, estrategia):
        if usuario not in cls._instancias:
            cls._instancias[usuario] = Recomendador(usuario, estrategia)
        return cls._instancias[usuario]

    def __init__(self, usuario, estrategia):
        self.usuario = usuario
        self.estrategia = estrategia

    '''def match(self, item, media_sesion, umbral=0.2):
        atributos = item.atributosSonoros  # o combinación con sentimentales
        
        return all(
            abs(atributos[key] - media_sesion[key]) < umbral
            for key in media_sesion
        )
'''
    def match(self, item, datos, umbral=0.2):
        atributos = {**item.atributosSonoros, **item.atributosSentimentales}
    # 1. comprobar atributos líderes
        lider_ok = all(
            atributos[k] >= datos["promedio_top"]
            for k in datos["atributos_lider"]
        )
        # 2. comprobar media global similar
        media_item = sum(atributos.values()) / len(atributos)
        media_ok = abs(media_item - datos["promedio_total"]) < umbral
        return lider_ok and media_ok

    def recomendar(self, lista, media_sesion):
        return self.estrategia.buscar(
            lista,
            lambda x: self.match(x, media_sesion)
        )