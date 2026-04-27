from catalogo import Catalogo
from cancion import Cancion
from usuario import Usuario
from artista import Artista
from playlist import PlayList

import random
import json
from datetime import datetime


# ---------------- CANCIONES ----------------
def cargar_canciones():
    canciones = []
    with open("canciones.json", "r") as f:
        data = json.load(f)
        for item in data:
            c = Cancion(item["nombre"],datetime.strptime(item["fecha"], "%Y-%m-%d"),item["autor"],
                item["id"],item["atributosSonoros"],item["atributosSentimentales"]
                )
            canciones.append(c)
    return canciones


# ---------------- ARTISTAS ----------------
def cargar_artistas(catalogo):
    artistas = []
    with open("artistas.json", "r") as f:
        data = json.load(f)
        for item in data:
            canciones = [next(c for c in catalogo.list_canciones if c.id == cid)
                for cid in item["canciones"]
                ]
            artista = Artista(item["nombre"],item["fechaNacimiento"],canciones)
            artistas.append(artista)

    return artistas


# ---------------- PLAYLIST ----------------
def cargar_playlists(catalogo):
    playlists = []
    with open("playlists.json", "r") as f:
        data = json.load(f)
        for item in data:
            canciones = [next(c for c in catalogo.list_canciones if c.id == cid)
                for cid in item["canciones"]]
            p = PlayList(item["titulo"],item["fechaCreacion"],canciones)
            playlists.append(p)
    return playlists


# ---------------- MAIN ----------------
def main():
    print("HelloWord")

    catalogo = Catalogo()

        # ---------------- CARGA CANCIONES ----------------
    try:
        canciones = cargar_canciones()
    except Exception as e:
        print(f"Ocurrió un error cargando canciones: {e}")
        canciones = []   # 🔥 evita crash

    for c in canciones:
        catalogo.agregar_cancion(c)

    # ---------------- CARGA ARTISTAS ----------------
    try:
        catalogo.list_artistas = cargar_artistas(catalogo)
    except Exception as e:
        print(f"Ocurrió un error cargando artistas: {e}")
        catalogo.list_artistas = []

    # ---------------- CARGA PLAYLISTS ----------------
    try:
        catalogo.list_playlists = cargar_playlists(catalogo)
    except Exception as e:
        print(f"Ocurrió un error cargando playlists: {e}")
        catalogo.list_playlists = []

    # ---------------- USUARIO ----------------
    user = Usuario("Juan")
    user.cargar_cancion_actual(1, "2025", "10:00")

    user = Usuario("Juan")
    user.cargar_cancion_actual(1, "2025", "10:00")

    while True:
        eleccion = input(
            "\n1) Ver Canciones\n2) Elegir Cancion\n3) Cancion aleatoria\n4) Recomendar\n0) Salir\n"
        )

        if eleccion == "1":
            for c in catalogo.list_canciones:
                print(c.nombre)

        elif eleccion == "2":
            nombre = input("Nombre de la canción: ")
            for c in catalogo.list_canciones:
                if c.nombre == nombre:
                    user.escuchar(c)
                    print("Añadida a sesión")

        elif eleccion == "3":
            c = random.choice(catalogo.list_canciones)
            user.escuchar(c)
            print("Escuchando:", c.nombre)

        elif eleccion == "4":
            media = user.cancion_actual.calcular_media()

            if not media:
                print("No hay canciones en la sesión")
                continue

            rec = user.recomendador.recomendar(
                catalogo.list_canciones,
                media
            )

            if rec:
                print("Recomendado:", rec.nombre)
            else:
                print("No encontrado")

        elif eleccion == "0":
            break


if __name__ == "__main__":
    main()