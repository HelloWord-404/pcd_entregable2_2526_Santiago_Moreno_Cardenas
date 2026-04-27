class Busqueda_Temporal(Estrategia):
    def buscar(self, lista, funcion_match):
        lista_ordenada = sorted(lista, key=lambda x: x.fechaCreacion, reverse=True)
        return next((x for x in lista_ordenada if funcion_match(x)), None)