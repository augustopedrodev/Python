tabuada = 1
while tabuada <= 10:
    numero = 1 
    print("\nTabuada do: ", tabuada)
    while numero <= 10:
        print(("%d x %d = %d") %(tabuada, numero, tabuada * numero))
        numero += 1
    tabuada +=1