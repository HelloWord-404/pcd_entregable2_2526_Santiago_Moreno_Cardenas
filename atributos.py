class Atributos:
    def __init__(self, felicidad, tristeza, nostalgia, letra,
                 agresividad, inspiracion,
                 ritmo, velocidad, energetica,
                 intensidad, tono, bailabilidad):

        # Sentimentales
        self.felicidad = float(felicidad)
        self.tristeza = float(tristeza)
        self.nostalgia = float(nostalgia)
        self.letra = float(letra)
        self.agresividad = float(agresividad)
        self.inspiracion = float(inspiracion)

        # Sonoros
        self.ritmo = float(ritmo)
        self.velocidad = float(velocidad)
        self.energetica = float(energetica)
        self.intensidad = float(intensidad)
        self.tono = float(tono)
        self.bailabilidad = float(bailabilidad)