# print("Hello World!");#
# aula else (condiciocional senao) exemplo abaixo#
distancia = float(input("Qual e a distancia que voce deseja percorrer em KM?"));
if distancia <= 200:
    pas = distancia * 0.50
    print("O valor da passagem sera: ", pas)
else:
    pas = distancia * 0.45
    print("O valor da passagem sera:", pas)