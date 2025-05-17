# try:
#     num1 = int(input())
#     num2 = int(input())
#     soma = num1 + num2
# except ValueError:
#     print("Você digitou algo que não é um numero!")
# else:
#     print("O valor da soma é: ", soma)

def dividir_numeros():
    while True:
        try:
            num3 = float(input())
            num4 = float(input())
            divisao = num3 / num4

        except ValueError:
            print("vc digitou algo que não é um numero!")
        except ZeroDivisionError:
            print("Divisão por erro não existe")
        else:
            print("o resultado da divisão é: ", divisao)
            break

def pergunta_numero():
    aux = 1
    while True:
        try:
            numero = int(input("digite um numero inteiro: "))
        except ValueError:
            print("Erro: isso não é um numero inteiro")
        else:
            print("O numero digitado foi: ")
        finally:
            print("tentativa de numero", aux)
            aux = + 1

# dividir_numeros()
pergunta_numero()