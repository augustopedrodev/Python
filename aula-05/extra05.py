codigo = int(input("Qual seu cargo ? 1-Escriturario, 2- Secretario, 3-Caixa, 4-Gerente, 5-Diretor,"))
sal = float(input("Qual seu salario? "))
if codigo == 1:
    aumento = 50
    novosal = sal + (sal * aumento)/100
    print(f"Seu novo salario é {novosal} com aumento de {aumento}%, com o cargo de Escriturario")
elif codigo == 2:
    aumento = 35
    novosal =sal + (sal * aumento)/100
    print(f"Seu novo salario é de {novosal} com aumento de {aumento}%, com o cargo de Secretario")
elif codigo == 3:
    aumento = 20
    novosal = sal + (sal * aumento)/100
    print(f"Seu novo salario é de {novosal} com aumento de {aumento}% com o cargo de Caixa")
elif codigo == 4:
    aumento = 10
    novosal = sal + (sal * aumento)/100
    print(f"Seu novo salario é de {novosal} com aumento de {aumento}% com cargo de Gerente")
elif codigo == 5:
    print("Voce não obteve aumento e nem um novo salario, seu cargo é de Diretor")
else:
    print("Codigo não existente")