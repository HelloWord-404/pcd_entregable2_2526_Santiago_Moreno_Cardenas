class PlayList:
    def __init__(self, titulo, fechaCreacion, canciones=None):
        self.titulo = titulo
        self.__fechaCreacion = fechaCreacion 
        self.lista_canciones = canciones if canciones is not None else []

    def agregar_cancion(self, cancion):
        self.lista_canciones.append(cancion)
    