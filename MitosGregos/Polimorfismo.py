class DeusesGregos:
    def __init__(self, forma_habitual):
        self.forma_habitual = forma_habitual
    
    def get_forma_habitual(self):
        return f"Forma habitual de um deus é a {self.forma_habitual}"
    
class Zeus(DeusesGregos):
    def __init__(self, forma_habitual, transmutacao):
        self.transmutacao = transmutacao
        super().__init__(forma_habitual)
        
    def get_transmutacao(self):
        if self.transmutacao == 1:
            return f"A forma que Zeus usou para conquistar Dânae foi de chuva."
        elif self.transmutacao == 2:
            return f"A forma que Zeus usou para conquistar Alcmena foi a do Anfitrião."

transmutacao_Zeus = Zeus('humanoide',1)
print(transmutacao_Zeus.get_transmutacao())