"""from atributos import Atributos
from caracteristicas import Caracteristicas

class Calculo_Atributos:
    def __init__(self):
        self.clasificacion = clasificacion
        self.puntajeTotal = PuntajeTotal

    def definirAtributos():
        atributosCancion = Atributos(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6 )
        lista_valores = list(vars(atributosCancion).values())
        lista_Atributos = list(vars(Caracteristicas).values())
        promedioTotal = (sum(lista_valores)/lista_valores.len())#devolver recomendador
        valoresMaximos = []
        posicionesMaximas = []#devolver a clase recomendador
        atributosLider = []
        for i in 3:
            valoresMaximos.append(max(lista_valores))
            posicion = lista_valores.index(valoresMaximos)
            posicionesMaximas.append(posicion)
            lista_valores[posicion] = 0
        promediovaloresMaximos = (sum(valoresMaximos)/4) #devolver a clase recomendador
        
        for i in 4:
            atributosLider.append(lista_Atributos[i])

"""

from atributos import Atributos

class Calculo_Atributos:

    def definirAtributos(self, atributosCancion):

        # 1. unir todos los atributos en una sola lista
        lista_valores = list(vars(atributosCancion).values())

        # 2. encontrar TOP 3 valores
        valores_maximos = []
        valores_temp = lista_valores.copy()

        for _ in range(3):
            max_val = max(valores_temp)
            valores_maximos.append(max_val)
            valores_temp.remove(max_val)

        promedio_top = sum(valores_maximos) / 3

        # 3. obtener posiciones (índices)
        lista_keys = list(vars(atributosCancion).keys())

        posiciones_maximas = []

        for val in valores_maximos:
            idx = lista_valores.index(val)
            posiciones_maximas.append(lista_keys[idx])

        # 4. promedio total
        promedio_total = sum(lista_valores) / len(lista_valores)

        return {
            "promedio_top": promedio_top,
            "atributos_lider": posiciones_maximas,
            "promedio_total": promedio_total
        }
        