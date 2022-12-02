import jogo_forca
import jogo_adivinhacao


def escolhe_jogo():
    print("********************************************************************************")
    print("*****************************Escolha o seu jogo!********************************")
    print("********************************************************************************")

    print("Escolha o seu jogo: (1) forca, (2) Adivinhação")

    jogo = int(input("Qual jogo você deseja jogar? "))

    if (jogo == 1):
        print("jogando Forca")
        jogo_forca.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação")
        jogo_adivinhacao.jogar()


if (__name__ == "__main__"):
    escolhe_jogo()
