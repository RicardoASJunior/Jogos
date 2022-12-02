

def jogar():

    import random

    numero_secreto = round(random.random() * 100)
    numero_de_tentativas = 0
    tentativa = 1

    print("*************************************************************************************")
    print("Bem vindo ao Jogo de adivinhação! O seu objetivo é descobrir qual é o número secreto!")
    print("O número secreto está entre 0 e 100")
    print("*************************************************************************************")

    comeco = int(input("Para começar digite 1: "))
    nivel= int(input("Para nível fácil[1], Médio[2], Difícil[3]: "))

    if(nivel == 1):
        numero_de_tentativas = 12
    if(nivel == 2):
        numero_de_tentativas = 8
    if(nivel == 3):
        numero_de_tentativas = 5

    if(comeco == 1):

        while (tentativa <= numero_de_tentativas):

            print("tentativa", tentativa , "de ",numero_de_tentativas)
            chute = int(input("Digite seu chute: "))
            igual = chute == numero_secreto
            maior = chute > numero_secreto
            menor = chute < numero_secreto
            if (igual):
                print("Você descobriu o número secreto!")
                break
            else:
                if (menor):
                    print("Você errou, o número sercreto é maior que", chute)

                elif (maior):
                    print("Você errou, o número sercreto é menor que", chute)
            tentativa = tentativa + 1

    print ("O número secreto é:" , numero_secreto)
    print("FIM DE JOGO!")

if (__name__ == "__main__"):
    jogar()