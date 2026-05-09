from busqueda_Aleatoria import BusquedaAleatoria
from busqueda_Temporal import Busqueda_Temporal
from busqueda_Alfabetica import Busqueda_Alfabetica
from datetime import datetime
from catalogo import Catalogo
from cancion import Cancion
from usuario import Usuario
from artista import Artista
from playList import PlayList
from estrategia import Estrategia

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
        op = input("\n1) Ver canciones\n2) Elegir\n3) Aleatoria\n4) Recomendar\n5) Cambiar estrategia\n6) Recomendar artistas\n7) Recomendar PlayList\n0) Salir\n")

        if op == "1":
            for c in catalogo.list_canciones:
                print(f"({c.id}) -> {c.nombre}")

        elif op == "2":
            id_s = int(input("id: "))
            for c in catalogo.list_canciones:
                if c.id == id_s:
                    user.cargar_cancion_actual(c, datetime.now().date(), datetime.now().time())
                    #user.escuchar(c)
                    
                    print("Añadida al historial")
            print("Total en sesión:" )
            for i in user.sesion_actual.canciones_durante_session:
                print(" ->",i.cancion.nombre,"")
        elif op == "3":
            c = random.choice(catalogo.list_canciones)
            user.cargar_cancion_actual(c, datetime.now().date(), datetime.now().time())
            print("Escuchando:", c.nombre)
            print("Total en sesión:")
            for i in user.sesion_actual.canciones_durante_session:
                print(" ->",i.cancion.nombre,"")

        elif op == "4":
            # canciones escuchadas
            print("\nCanciones escuchadas en la sesión actual:")

            for i in user.sesion_actual.canciones_durante_session:
                print("-->", i.cancion.nombre)

            # calcular datos de la sesión
            datos = user.sesion_actual.calcular_media()

            if not datos:
                print("Escucha canciones primero")
                continue

            print("\nLideres:", datos["atributos_lider"])
            print("cimas lideres:", round(datos["promedio_top"], 2), "(valores lideres superiores a este promedio se consideran buenas coincidencias)")
            print("Media sesión:", round(datos["promedio_total"], 2))
            


            # recomendaciones
            recomendaciones = user.recomendador.recomendar(
                catalogo.list_canciones,
                datos
            )

            print("\nRecomendadas:")

            for i, c in enumerate(recomendaciones):
                print(i + 1, "-", c.nombre)

            # elegir
            opcion = int(input("\nElige una canción: ")) - 1

            if 0 <= opcion < len(recomendaciones):

                seleccion = recomendaciones[opcion]

                user.cargar_cancion_actual(
                    seleccion,
                    datetime.now().date(),
                    datetime.now().time()
                )

                print("Escuchando:", seleccion.nombre)
                print(seleccion.atributosSentimentales,"\n",seleccion.atributosSonoros)
            else:
                print("Cancion no valida")

        elif op == "5":

            print("\nEstrategias disponibles:")
            print("1 - Aleatoria")
            print("2 - Alfabetica")
            print("3 - Temporal")

            e = input("Elige estrategia: ")

            if e == "1":
                user.cambiar_estrategia(BusquedaAleatoria())
                print("Estrategia cambiada")
            elif e == "2":
                user.cambiar_estrategia(Busqueda_Alfabetica())
                print("Estrategia cambiada")
            elif e == "3":
                user.cambiar_estrategia(Busqueda_Temporal())
                print("Estrategia cambiada")
            else:
                print("Opción no válida")
        
        elif op == "6":

            datos = user.sesion_actual.calcular_media()

            if not datos:
                print("Escucha canciones primero")
                continue

            print("\nArtistas recomendados:\n")

            artistas_match = []

            for artista in catalogo.list_artistas:

                score = 0

                for cancion in artista.lista_Canciones:

                    atributos = cancion.atributosSonoros.copy()
                    atributos.update(cancion.atributosSentimentales)

                    for k in datos["atributos_lider"]:

                        if atributos[k] >= datos["promedio_top"]:
                            score += 1

                artistas_match.append((score, artista))

            artistas_match.sort(key=lambda x: x[0], reverse=True)

            artistas = [a[1] for a in artistas_match]

            top_artistas = user.estrategia.buscar(artistas)

            for i, a in enumerate(top_artistas):
                print(i + 1, "-", a.nombre)

            opcion = int(input("\nElige un artista: ")) - 1

            if 0 <= opcion < len(top_artistas):

                artista = top_artistas[opcion]

                print("\nReproduciendo canciones de:", artista.nombre)

                for c in artista.lista_Canciones:
                    print("->", c.nombre)

            else:
                print("Artista no válido")
        
        elif op == "7":

            datos = user.sesion_actual.calcular_media()

            if not datos:
                print("Escucha canciones primero")
                continue

            print("\nPlaylists recomendadas:\n")

            playlists_match = []

            for playlist in catalogo.list_playlists:

                score = 0

                for cancion in playlist.lista_canciones:

                    atributos = cancion.atributosSonoros.copy()
                    atributos.update(cancion.atributosSentimentales)

                    for k in datos["atributos_lider"]:

                        if atributos[k] >= datos["promedio_top"]:
                            score += 1

                playlists_match.append((score, playlist))

            playlists_match.sort(key=lambda x: x[0], reverse=True)

            playlists = [p[1] for p in playlists_match]

            top_playlists = user.estrategia.buscar(playlists)

            for i, p in enumerate(top_playlists):
                print(i + 1, "-", p.titulo)

            opcion = int(input("\nElige una playlist: ")) - 1

            if 0 <= opcion < len(top_playlists):

                playlist = top_playlists[opcion]

                print("\nReproduciendo playlist:", playlist.titulo)

                for c in playlist.lista_canciones:
                    print("->", c.nombre)

            else:
                print("Playlist no válida")


        elif op == "0":
            print("Cancion no encontrada")
            break


if __name__ == "__main__":
    main()