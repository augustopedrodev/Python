pontos = 0
questao = 0
while questao <= 3:
    resposta =input(str("Resposta da questao %d: " % questao))
    if questao ==  1 and (resposta == "b" or resposta == "B"):
        pontos = pontos + 1
    if questao == 2 and (resposta == "a" or resposta == "A"):
        pontos = pontos + 1
    if questao == 3 and (resposta =="c" or resposta == "C"):
        pontos = pontos + 1
    questao += 1
    print("O aluno fez %d ponto(s)" % pontos)