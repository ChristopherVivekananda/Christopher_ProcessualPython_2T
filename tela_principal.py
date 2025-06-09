nome = "Rafael"
idade = 19
cpf = 14962035096
telefone = 8734248448
email = "gabriel.games@gmail.com"
saldo = 3
reserva = 21
cripto = 51 *-0.000112
investimentos = 4 *0.0004
seguros = 2
histrans = 4

print("Bem vindo de volta", nome)
if saldo > 0:
    print("Saldo Disponível:", "R$", saldo)
elif saldo == 0:
    print("Você está sem saldo!")
else:
    print("Seu saldo está negativado!")

if reserva > 0:
    print("Sua Reserva:", "R$",reserva)
else:
    print("Você não tem nenhum dinheiro reservado, faça sua reserva gratuitamente!")
if cripto > 0:
    print("Suas criptomoedas renderam", "R$", cripto, "Hoje!")
elif cripto == 0:
    print("Você não tem nehuma reserva de cripto, faça uma!")
else:
    print("Suas criptomoedas perderam", "R$", cripto, "Em valor hoje!")
   
if investimentos > 0:
    print("Seus investimetos renderam", "R$", investimentos, "hoje!")
    investimento_ver = input("Ver investimentos (escreva sim ou não): ")
    if investimento_ver == "sim":
        print("Borracharia Pereira: R$ 2, \nRoberto Lanches: R$ 1, \nRaimundo Palmeiras Bar")
    elif investimento_ver == "não":
        print("Prossiga")
    else:
        print("error escreva novamente")
        investimento_ver = input("Ver investimentos (escreva sim ou não): ")
        if investimento_ver == "sim":
            print("Borracharia Pereira: R$ 2, \nRoberto Lanches: R$ 1, \nRaimundo Palmeiras Bar")
        elif investimento_ver == "não":
            print("Prossiga")

else:
    print("Você não tem nenhum dinheiro investido, faça seu CDB a partir de R$1!")
   
if seguros > 0:
    print("Você tem:",seguros, "seguros em seu nome")
    seguros_ver = input("Ver seguros (escreva sim ou não): ")
    if seguros_ver == "sim":
        print("Seguro de Vida\nSeguro do Carro")
    elif seguros_ver == "não":
        print("Prossiga")
    else:
        print("error")

if histrans > 0:
    print("Você tem", histrans, "transferências em seu histórico")
    hist_ver = input("Ver Histórico (escreva sim ou não): ")
    if hist_ver == "sim":
        print("joão Café\nBanco Monedas\nJúlio Moreira\nJânio Junior Morais")
    elif hist_ver == "não":
        print("Prossiga")
    else:
        print("error")
else:
    print("Histórico Zerado")
