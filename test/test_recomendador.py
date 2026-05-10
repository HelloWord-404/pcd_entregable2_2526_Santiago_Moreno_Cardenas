from recomendador import Recomendador
from estrategia import Estrategia

class FakeEstrategia(Estrategia):
    def buscar(self, lista):
        return lista[:1]

class FakeUsuario:
    def __init__(self):
        self.sesion_actual = type(
            "Sesion",
            (),
            {"canciones_durante_session": []}
        )()

def test_recomendador_basico():

    r = Recomendador(
        FakeUsuario(),
        FakeEstrategia()
    )

    resultado = r.recomendar([], None)

    assert resultado == []