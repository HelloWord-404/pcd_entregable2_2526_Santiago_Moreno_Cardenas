from cancion import Cancion
import pytest

def test_creacion_cancion():

    c = Cancion(
        "Song1",
        "2024-01-01",
        "Autor1",
        1,
        {"energia": 0.8},
        {"felicidad": 0.7}
    )

    assert c.nombre == "Song1"
    assert c.id == 1