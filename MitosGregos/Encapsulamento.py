class AcessoOlimpo:
    def __init__(self, status):
        self.status = status
    
    def __olimpo(self):
        return f"Somente os deuses tem acesso."
    
    def terra(self):
        return f" Os deuses e os seres vivos tem acesso."
    
    def acessar_olimpo(self, deuses):
        if deuses == 'Era' and self.status == 'deus':
            return self.__olimpo()
        
        return f"Você não tem acesso ao Olimpo."
    
    
era = AcessoOlimpo('deus')
acesso_era = era.acessar_olimpo('Era')
print(acesso_era)

icaro = AcessoOlimpo('humano')
acesso_icaro = icaro.acessar_olimpo('Icaro')
print(acesso_icaro)    
        