class Session_Actual:
    def __init__(self, id, fecha, hora):
        self.id = id
        self.fecha = fecha
        self.hora = hora
        self.canciones_durante_session = []  # Lista de canciones

    def agregar_cancion_escuchada(self, cancion):
        self.canciones_durante_session.append(cancion)