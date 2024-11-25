casa = float(input("Quantos reais está avaliada a casa?"))
sal = float(input("Qual seu salario? "))
finan = float(input("Em quantos anos deseja pagar? "))
meses = finan * 12 
prestacao = casa / meses
if prestacao <= sal * 0.30:
    print(prestacao)
    print("Será possivel financiar sua casa nova!!")
else:
    print("Não é possivel fazer financiamento")