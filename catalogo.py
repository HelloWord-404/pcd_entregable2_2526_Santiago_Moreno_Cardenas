class Catalogo:
    def __init__(self):
        self.list_canciones = []  
        self.list_artistas = []   
        self.list_playlists = []  

    # ---------------- CANCIONES ----------------
    def agregar_cancion(self, cancion):
        self.list_canciones.append(cancion)
    
    def eliminar_cancion(self, cancion):
        if cancion in self.list_canciones:
            self.list_canciones.remove(cancion)

    # ---------------- ARTISTAS ----------------
    def agregar_artista(self, artista):
        self.list_artistas.append(artista)

    def eliminar_artista(self, artista):
        if artista in self.list_artistas:
            self.list_artistas.remove(artista)

    # ---------------- PLAYLIST ----------------
    def agregar_PlayList(self, playlist):
        self.list_playlists.append(playlist)
    
    def eliminar_PlayList(self, playlist):
        if playlist in self.list_playlists:
            self.list_playlists.remove(playlist)