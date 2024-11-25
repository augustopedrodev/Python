nota1 = float(input("Qual sua primeira nota? "))
nota2 = float(input("Qual sua segunda nota? "))
nota3 = float(input("Qual sua terceira nota? "))
media = (nota1 + nota2 + nota3)/3
if media < 6:
    print("Voce foi reprovado!")
elif media >= 6:
    print("Voce foi aprovado!")
else:
    print("Numeros não validos!")