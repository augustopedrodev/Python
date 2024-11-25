operacao = int(input("Qual operação voce deseja fazer? 1- Soma, 2- Sub, 3- Multi, 4- Div: "))
a = float(input("Qual o primeiro numero: "))
b = float(input("Qual o segundo numero: "))
if operacao == 1:
    operacao = a + b
    print(operacao)
elif operacao == 2:
    operacao = a - b
    print(operacao)
elif operacao == 3:
    operacao = a * b
    print(operacao)
elif operacao == 4:
    operacao = a / b
    print(operacao)
else:
    print("Operação não existente")