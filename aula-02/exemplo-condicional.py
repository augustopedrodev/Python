fab = int(input("Qual é o ano de fabricacao do seu carro: "))
ano_atual = int(input ("Qual é o ano atual? "))
idade = ano_atual - fab
if idade  <= 3: 
    print("Seu carro é novo ")
if idade > 3:
    print("Seu carro é velho")