import math
try:
    number = int(input("Numero: "))
    if number < 0:
        raise ValueError('Numero menor que zero')
    resultado = math.sqrt(number)
    print(f"O resultado é {resultado}") 

    numerador = int(input("Numerador: "))
    denominador = int(input("Denominador: "))
    if denominador == 0:
        raise ZeroDivisionError('Numero igual zero')
    resultado = numerador / denominador
    print(f"O resultado é {resultado}") 
    
    number = int(input("Digite um número: "))
    print("O número digitado foi: ", number)
    
except ValueError:
     print('Numero invalido')   
except ZeroDivisionError:
    print("Não é possível dividir um número por zero")
except (TypeError):
    print("Erro nos tipos de dados que você digitou")
except KeyboardInterrupt:
    print("Dados não informados")
except Exception as err:
    print(f"Ocorreu uma exceção: {err}")
finally:
    print("Obrigada!")
    
#Exercicio 5: erro de importação (SyntaxError: invalid syntax)