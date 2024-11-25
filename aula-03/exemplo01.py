minutos = int(input("Quantos minutos voce utilizou esse mes: "))
if minutos < 200:
    preco = 0.20
else: 
    if minutos < 400:
        preco = 0.18
    else:
        preco = 0.15
print("Voce vai pagar esse mes: R$%6.2f" % (minutos * preco))