idade = int(input("Qual sua idade: "))
convite = int(input("Voce tem o convite: 1- Sim, 2-Não: "))
if idade >= 18 and convite == 1:
    print("Voce pode entrar no evento")
else:
    print("Voce não pode entrar no evento")