class Humano:
    def __init__(self, nome, cidade, status, oraculo):
        self.nome = nome
        self.cidade = cidade
        self.status = status
        self.oraculo = oraculo
    
    
    def get_nome(self):
        return f"Seu é {self.nome}"
    
    
    def get_cidade(self):
        return f"Ele é {self.status} de {self.cidade}"
    
class Edipo(Humano):
    def __init__(self, nome, cidade, status, oraculo, tipo_maldicao):
        self.tipo_maldicao = tipo_maldicao
        
        super().__init__(nome, cidade, status, oraculo)
        
    def get_maldicao(self):
        if self.tipo_maldicao == 1:
            return f"Sua maldição é o fim da sua linhagem."
        elif self.tipo_maldicao == 2:
            return f"Sua maldição é matar o seu pai e casar com a sua mãe."

edipo = Edipo('Édipo', 'Tebas', 'Rei', 'Delfos', 2)
print(edipo.get_maldicao())        
