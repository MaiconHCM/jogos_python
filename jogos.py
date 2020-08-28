import advinhacao
import forca

def selecionar_jogo():
    print("Selecione o jogo que deseja jogar:\n1-Advinhação\n2-Forca")
    jogo_selecionado=int(input("Defina sua opção...\n"))

    if(jogo_selecionado==1):
        advinhacao.jogar()
    else:
        forca.jogar()

if(__name__=='__main__'):
    selecionar_jogo()