idade = int(input("Qual sua idade? "))
if idade < 16:
    print("Voce nao é eleitor")
elif idade >= 16 and idade < 18 or idade >= 65:
    print("Voce é eleitor facultativo")
elif idade >= 18 and idade < 65:
    print("Voce é um eleitor obrigatorio")
    