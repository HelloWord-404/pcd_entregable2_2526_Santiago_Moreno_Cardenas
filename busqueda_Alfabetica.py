class Busqueda_Alfabetica(Estrategia):
    def buscar(self, lista, funcion_match):
        lista_ordenada = sorted(lista, key=lambda x: x.nombre)
        return next((x for x in lista_ordenada if funcion_match(x)), None)