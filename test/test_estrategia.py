from busqueda_Alfabetica import Busqueda_Alfabetica

class Dummy:
    def __init__(self, nombre):
        self.nombre = nombre

def test_orden_alfabetico():

    e = Busqueda_Alfabetica()

    lista = [Dummy("C"), Dummy("A"), Dummy("B")]

    res = e.buscar(lista)

    assert res[0].nombre == "A"