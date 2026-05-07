#from usuario import Usuario


class Recomendador:
    _instancias = {}  # guarda recomendadores por usuario

    @classmethod
    def obtener_instancia(cls, usuario, estrategia):
        if usuario not in cls._instancias:
            cls._instancias[usuario] = Recomendador(usuario, estrategia)
        else:
            cls._instancias[usuario].estrategia = estrategia  # actualización de stregias
        return cls._instancias[usuario]

    def __init__(self, usuario, estrategia):
        self.usuario = usuario
        self.estrategia = estrategia

    
    
    def match(self, item, datos):

        atributos = item.atributosSonoros.copy()
        atributos.update(item.atributosSentimentales)

        promedio = sum(atributos.values()) / len(atributos)

        score = 0

        for k in datos["atributos_lider"]:

            if atributos[k] >= datos["promedio_top"]:
                score += 1

        # al menos 1 de los líderes deben cumplirse
        return score >= 1 and abs(promedio - datos["promedio_total"]) < 0.6



    def recomendar(self, lista, media_sesion):

        escuchadas = set(
            i.cancion.id for i in self.usuario.sesion_actual.canciones_durante_session)


        candidatos = []
        for item in lista:

            if item.id in escuchadas:
                continue

            if self.match(item, media_sesion):
                candidatos.append(item)
            if not candidatos:
                return []
        return self.estrategia.buscar(candidatos)