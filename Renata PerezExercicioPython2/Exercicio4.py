class Professor:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
    
    def __valor_salario (self):
        return f"O valor do salário do {self.nome} é {self.salario}."
    
    def acessar_salario(self, profissao):
        if profissao == 'professor' and self.nome == 'Joao da Silva':
            return self.__valor_salario()
        
        return f"Você não tem acesso ao valor so salário."
    
joao = Professor('Joao da Silva', 50, 4500.00)
acesso_joao = joao.acessar_salario('professor')
print(acesso_joao)

jose = Professor('José Santos', 55, 4900.00)
acesso_jose = jose.acessar_salario('professor')
print(acesso_jose)