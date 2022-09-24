from csv import DictReader
import json

def ler_arquivo_csv():
    with open ("musicas.csv","r") as arq_csv:
        leitor_csv = DictReader(arq_csv)
        registros = [
            registro
            for registro in leitor_csv
        ]
        print(registros)
    return registros
   
def salvar_arquivos_json(registros):
    with open("saida.json","w") as arq_json:
        json.dump(registros,arq_json)
    
def principal():
    registros = ler_arquivo_csv()
    salvar_arquivos_json(registros)
    #salvar_arquivos_json(registros)
    
if __name__ == "__main__":
    principal()