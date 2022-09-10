class Quadrado:
    def __init__(self,lado):
        self.lado = lado
        
    
    def get_area_quadrado(self):
        area_quadrado = self.lado ^ 2
        return f"A área do quadrado é {area_quadrado} m²."
    
    def get_perimetro_quadrado(self):
        perimetro_quadrado = self.lado * 4
        return f"O perimetro do quadrado é {perimetro_quadrado} m."