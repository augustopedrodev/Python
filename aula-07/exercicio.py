mes = 1
depinicial = float(input("qual o deposito inicial? "))
juros = float(input("Qual o juros ao mes que o Banco trabalha? "))
while mes == 24:
    print("O mes é %d " %mes)
    valor = 24 * juros
    mes = mes + 1
print(f"O valor final recebido será de: {valor} ")