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
        
class PessoaFisica(Pessoa):
    def __init__(self, tipo_pessoa, cpf, nome, idade, cidade_nascimento):
        self.cidade_nascimento = cidade_nascimento
        
        super().__init__(tipo_pessoa, cpf, nome, idade)
    
    def get_dados_pessoa_fisica(self):
        return f"A cidade de nascimento de {self.nome} é {self.cidade_nascimento}."
    
maria = PessoaFisica('F', '123.456.789-11', 'Maria Silva', 45, 'São Paulo')
print(maria.get_dados_pessoa_fisica())