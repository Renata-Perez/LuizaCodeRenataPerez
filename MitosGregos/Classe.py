class DeusesGregos:
    def __init__(self, nome, caracteristica, poder, territorio):
        self.nome = nome
        self.caracteristica = caracteristica
        self.poder = poder
        self.territorio = territorio
        
        
    def get_protetor(self):
        return f"O(a) deus(a) {self.nome} protetor(a) de {self.territorio}"
    
    
    def get_dever(self):
        return f"Ajudar os seres humanos de {self.territorio}"

    
atena = DeusesGregos('Atena',
                     'senso de justiça',
                     'sabedoria e estratégia',
                     'Atenas')

apolo = DeusesGregos('Apolo',
                     'divindade solar e das artes',
                     'afastar a morte',
                     'Troia')    
       
protetor = atena.get_protetor()
print(protetor)

dever = apolo.get_dever()
print(dever)
