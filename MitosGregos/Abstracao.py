import time

class Trabalhos:
    def __init__(self, skill, nome):
        self.skill = skill
        self.nome = nome
    
    def dose_trabalhos(self):
        print("Aguarde...")
        
        start = time.time()
        
        mensagem = f"Para se livrar da culpa {self.nome} teve que {self.skill}: "
        mensagem += f"matar o Leão de Nemeia em {time.time()}; "
        
        time.sleep(2)
        
        mensagem += f"matar a Hidra de Lerna em {time.time()}; "
        time.sleep(2)
        
        mensagem += f"capturar a corça de Cerineia em {time.time()}; "
        time.sleep(2)
        
        mensagem += f"capturar o javali de Erimanto em {time.time()}; "
        time.sleep(3)
        
        mensagem += f"limpar os estábulos de Aúgias em {time.time()}; "
        time.sleep(1)
        
        mensagem += f"matar as aves do lago Estínfalo em {time.time()}; "
        time.sleep(1)
        
        mensagem += f"matar o touro de Creta em {time.time()}; "
        time.sleep(2)
        
        mensagem += f"capturar os cavalos de Diomedes em {time.time()}; "
        time.sleep(1)
        
        mensagem += f"roubar o cinturão de Hipólita em {time.time()}; "
        time.sleep(2)
        
        mensagem += f"capturar o gado de Gerião em {time.time()}; "
        time.sleep(1)
        
        mensagem += f"capturar os pomos de ouro do Jardim das Hespérides {time.time()}; "
        time.sleep(1)
        
        mensagem += f"capturar o cão de Hades, Cérbero {time.time()}; "
        time.sleep(2)
        
        end = time.time()
        calculo_tempo = end - start

        return mensagem + f"E o tempo total gasto foi: {calculo_tempo}"
    
    
hercules = Trabalhos('executar 12 tarefas', 'Hercules')
print(hercules.dose_trabalhos())
        
        
        
        
    