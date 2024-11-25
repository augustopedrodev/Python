idade = int(input("Qual sua idade: "))
altura = float(input("Qual a altura: "))
soma_alt = 0;
soma_id = 0;
npessoas =0;

while (idade != 0 ):
    npessoas = npessoas + 1;
    soma_id = soma_id + idade;
    soma_alt = soma_alt + altura;
    idade = int(input("Informe a idade: "))
    if (idade != 0):
        altura = int(input("Informe a altura: "))
        
print(f"A media de idade é de: {soma_id/npessoas}")
print(f"A media de altura é de: {soma_alt/npessoas}")