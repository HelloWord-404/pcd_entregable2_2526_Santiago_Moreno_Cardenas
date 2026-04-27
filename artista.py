class Artista:
    def __init__(self, nombre, fechaNacimiento, canciones=None):
        self.nombre = nombre
        self.__fechaNacimiento = fechaNacimiento
        self.lista_Canciones = canciones if canciones is not None else []
    
    def agregar_cancion(self, cancion):
        self.lista_canciones.append(cancion)
    
    