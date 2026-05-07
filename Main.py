from datetime import datetime
from catalogo import Catalogo
from cancion import Cancion
from usuario import Usuario
from artista import Artista
from playList import PlayList

import json
import random


def main():
    print("HelloWord")
    catalogo = Catalogo()

    # -------- CARGAR CANCIONES --------
    try:
        with open("canciones.json") as f:
            data = json.load(f)

            for item in data:
                c = Cancion(
                    item["nombre"],
                    item["fecha"],
                    item["autor"],
                    item["id"],
                    item["atributosSonoros"],
                    item["atributosSentimentales"]
                )
                catalogo.agregar_cancion(c)

    except:
        print("Error cargando canciones")

    # -------- CARGAR ARTISTAS --------
    try:
        with open("artistas.json") as f:
            data = json.load(f)

            for item in data:
                canciones = []
                for cid in item["canciones"]:
                    for c in catalogo.list_canciones:
                        if c.id == cid: #
                            canciones.append(c) #agregamos la cancion al repertorio del artista

                a = Artista(item["nombre"], item["fechaNacimiento"], canciones)
                catalogo.list_artistas.append(a)

    except:
        print("Error cargando artistas")

    # -------- CARGAR PLAYLISTS --------
    try:
        with open("playlists.json") as f:
            data = json.load(f)

            for item in data:
                canciones = []
                for cid in item["canciones"]:
                    for c in catalogo.list_canciones:
                        if c.id == cid:
                            canciones.append(c) #solo agregamos las canciones que esten definidas en el catalgo
                p = PlayList(item["titulo"], item["fechaCreacion"], canciones)
                catalogo.list_playlists.append(p)

    except:
        print("Error cargando playlists")

    # -------- USUARIO --------
    user = Usuario("Santiago")
    #user.cargar_cancion_actual(1, "2025-05-07", "10:00")

    # -------- MENÚ --------
    while True:
        op = input("\n1 Ver canciones\n2 Elegir\n3 Aleatoria\n4 Recomendar\n0 Salir\n")

        if op == "1":
            for c in catalogo.list_canciones:
                print(f"({c.id}) -> {c.nombre}")

        elif op == "2":
            nombre = input("Nombre: ")
            for c in catalogo.list_canciones:
                if c.nombre == nombre:
                    user.escuchar(c)
                    print("Añadida al historial")
            print("Total en sesión:", len(user.cancion_actual.canciones_durante_session))

        elif op == "3":
            c = random.choice(catalogo.list_canciones)
            user.escuchar(c)
            print("Escuchando:", c.nombre)
            print("Total en sesión:", len(user.cancion_actual.canciones_durante_session))

        elif op == "4":
            media = user.cancion_actual.calcular_media()

            if media:
                rec = user.recomendador.recomendar(catalogo.list_canciones, media)
                if rec:
                    print("Recomendado:", rec.nombre)
                else:
                    print("No encontrado")
            else:
                print("Escucha canciones primero")

        elif op == "0":
            break


if __name__ == "__main__":
    main()