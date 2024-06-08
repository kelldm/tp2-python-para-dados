def divide_numeros():
    while True:
        try:
            num1 = float(input("Digite o primeiro numero: "))
            num2 = float(input("Digite o segundo numero: "))
            resultado = num1 / num2
        except ValueError:
            print("Erro: Entrada invalida. Por favor, insira um numero.")
            continue
        except ZeroDivisionError:
            print("Erro: Divisao por zero nao eh permitida. Tente novamente.")
            continue
        else:
            print(f"O resultado da divisao eh: {resultado}")
            break

divide_numeros()
