n = 0
m = 0
retirar = 0
pecas_atuais = 0
retirado = False
jogadaComputador = False
jogadaPlayer = False
jogando = False

def partida():
    global n
    global m
    n = int(input("digite o número de peças iniciais"))
    m = int(input("digite o número máximo de peças retiradas por jogada"))
    global pecas_atuais
    pecas_atuais = n
    jogando == True



def inicio(pecas_iniciais, maximo_pecas):
    if(pecas_iniciais % (maximo_pecas + 1) == 0):
        print("Por favor, comece voce!")
        usuario_escolhe_jogada(n,m, n)
    else:
        computador_escolhe_jogada(n, m, n)



def computador_escolhe_jogada(pecas_iniciais, maximo_pecas, t):
    for i in range(1, maximo_pecas):
        if((pecas_atuais - i) % (maximo_pecas + 1) == 0):
            retirarPeca(i)
            global retirado
            retirado = True
            print("restam: {} peças" .format(pecas_atuais))
    if(retirado == False):
        retirarPeca(maximo_pecas)
        print("restam: {} peças" .format(pecas_atuais))
    computadorJogar()



def usuario_escolhe_jogada(pecas_iniciais, maximo_pecas, t):
    retirar = int(input("insira o número de peças que deseja retirar"))
    if(retirar > maximo_pecas):
        print("número inválido")
    else:
         #global pecas_atuais
        retirarPeca(retirar)
        print("restam: {} peças" .format(t))
        jogadorJogar()



def retirarPeca(number):
    global pecas_atuais
    pecas_atuais -= number



def fimDeJogo():
    global jogando
    jogando = False
    if(jogadaComputador == True):
        print("Parabéns! Você venceu!!!")
    else:
        print("Poxa, você perdeu :(")

def computadorJogar():
    global jogadaComputador
    global jogadaPlayer
    jogadaComputador = True
    jogadaPlayer = False

def jogadorJogar():
    global jogadaComputador
    global jogadaPlayer
    jogadaComputador = False
    jogadaPlayer = True


partida()
inicio(n, m)

while(jogando):
    if(jogadaComputador):
        usuario_escolhe_jogada(n,m, pecas_atuais)
    else:
        computador_escolhe_jogada(n,m,pecas_atuais)


