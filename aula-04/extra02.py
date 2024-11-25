nome = str(input("Qual seu nome: "))
idade = int(input("Qual sua idade: "))
if idade <= 18:
    valor = 50.00 
    print(f"Olá {nome}, idade é {idade}, e sua mensalidade será no valor de {valor}")
elif idade >= 19 and idade <= 29:
    valor = 70.00 
    print(f"Olá {nome}, idade é {idade}, e sua mensalidade será no valor de {valor}")
elif idade >= 30 and idade <= 45:
    valor = 90.00 
    print(f"Olá {nome}, idade é {idade}, e sua mensalidade será no valor de {valor}")
elif idade >= 46 and idade <= 65:
    valor = 130.00 
    print(f"Olá {nome}, idade é {idade}, e sua mensalidade será no valor de {valor}")
elif idade > 65:
    valor = 170.00 
    print(f"Olá {nome}, idade é {idade}, e sua mensalidade será no valor de {valor}")