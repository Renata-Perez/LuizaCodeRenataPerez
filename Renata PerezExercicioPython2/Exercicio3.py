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

class PessoaJuridica(Pessoa):
    def __init__(self, tipo_pessoa, cpf, nome, idade, cnpj):
        self.cnpj = cnpj
        super().__init__(tipo_pessoa, cpf, nome, idade)
        
    def get_dados_pessoa_juridica(self):
        return f"Empresa de CNPJ: {self.cnpj}"
    
empresa_maria = PessoaJuridica('F', '123.456.789-11', 'Maria Silva', 45,'12.345.678/0001-99')
print(empresa_maria.get_dados_pessoa_juridica())