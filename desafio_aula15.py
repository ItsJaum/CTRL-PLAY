def  Atividade():
    try:    
        N = int(input())
        if n <= 1 or n >= 1000:
            print("erro: O intervalo deve estar entre 2 e 999")
        else:
            for i in range(1, n+1):
                print(i, i**2, i**3)
    except ValueError:
        print("Erro: Entrada invalida. Por favor, digite um numero inteiro.")

Atividade()

