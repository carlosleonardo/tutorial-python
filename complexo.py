print("Números complexos em Python")
try:
    num1 = complex(input("Digite o primeiro número complexo (ex: 2+3j): "))
    num2 = complex(input("Digite o segundo número complexo (ex: 1-4j): "))
    soma = num1 + num2
    subtracao = num1 - num2
    produto = num1 * num2
    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Produto: {produto}")
    print(f"Quociente: {num1 / num2}")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar números complexos no formato correto.")