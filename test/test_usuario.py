from usuario import Usuario

def test_usuario_crea_sesion():

    u = Usuario("Santiago")

    assert u.nombre == "Santiago"
    assert u.sesion_actual is not None