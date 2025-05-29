nome1 = input("coloque o nome aqui: ")
nome2 = input("coloque o nome aqui: ")
nome3 = input("coloque o nome aqui: ")
nome4 = input("coloque o nome aqui: ")
nome5 = input("coloque o nome aqui: ")
nome6 = input("coloque o nome aqui: ")
nome7 = input("coloque o nome aqui: ")
nome8 = input("coloque o nome aqui: ")
nome9 = input("coloque o nome aqui: ")
nome0 = input("coloque o nome aqui: ")

caracteres_invalidos = ["´", ",", "!", "@", "#", "$", "%", "&", "*", "(", ")", "=", "+", "[", "]", "{", "}", "|", "\\", "/", "?", "<", ">", ".", ";", ":", "\"", "'"]

lista = [nome1, nome2, nome3, nome4, nome5, nome6, nome7, nome8, nome9, nome0]

caractere_encontrado = False
for nome in lista:
    for caractere in caracteres_invalidos:
        if caractere in nome:
            print("Caractere inválido encontrado:", caractere)
            caractere_encontrado = True
            break
    if caractere_encontrado:
        break
if not caractere_encontrado:
    lista.sort()
    print(lista)
    for nome in lista:
        print(f"{nome}: {len(nome)} letras")
