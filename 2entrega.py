dia = 27
contador = 0
while contador <= 100:
    multiplicador = dia * contador
    print(contador, "x", dia ,"=", multiplicador)
    contador +=1
    if multiplicador >= 1000:
        print("maior que 1000")
