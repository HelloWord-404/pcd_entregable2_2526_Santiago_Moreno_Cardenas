from catalogo import Catalogo
from cancion import Cancion

def test_catalogo_agregar_cancion():

    catalogo = Catalogo()

    c = Cancion(
        "Song1",
        "2024-01-01",
        "Autor1",
        1,
        {"energia": 0.8},
        {"felicidad": 0.7}
    )

    catalogo.agregar_cancion(c)

    assert len(catalogo.list_canciones) == 1
    assert catalogo.list_canciones[0].nombre == "Song1"