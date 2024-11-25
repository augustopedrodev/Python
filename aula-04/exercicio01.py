kwh = float(input("Qual foi a quantidade consumida de KWH? "))
tipo = int(input("Qual seu tipo de instalação? Digite 1 para Residencia, 2 para comercio e 3 para industria: "))
if tipo == 1 and kwh <= 500:
    valor = kwh * 0.40
    print(valor)
elif tipo == 1 and kwh > 500:
    valor = kwh * 0.65
    print(valor)
elif tipo == 2 and kwh <= 1000:
    valor = kwh * 0.55
    print(valor)
elif tipo == 2 and kwh > 1000:
    valor = kwh * 0.60
    print(valor)
elif tipo == 3 and kwh <= 5000:
    valor = kwh * 0.55
    print(valor)
elif tipo == 3 and kwh > 5000:
    valor = kwh * 0.60
    print(valor)
else: 
    print("Tipo de instalação não encontrado, por favor digite 1 para residencia, 2 para comercio e 3 para industria!")