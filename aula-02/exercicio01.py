velocidade = int(input("Qual é a sua velocidade: "))
km = velocidade - 80
valor = km * 5
if velocidade <= 80:
    print("Voce está na velocidade correta!")
if velocidade > 80:
    print(f"Voce ira pagar {valor} reais em multa")