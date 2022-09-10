class Pessoa:
    def __init__(self, tipo_pessoa, cpf, nome, idade):
        self.tipo_pessoa = tipo_pessoa
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        
    def get_dados_pessoa(self):
        if self.tipo_pessoa == 'F':
            return f" A pessoa de CPF {self.cpf} e nome {self.nome} é fumante."
        elif self.tipo_pessoa == 'N':
            return f"A pessoa de CPF {self.cpf} e nome {self.nome} não é fumante."


maria = Pessoa('F', '123.456.789-11', 'Maria Silva', 45)
dados_maria = maria.get_dados_pessoa()
print(dados_maria)