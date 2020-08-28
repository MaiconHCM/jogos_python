import random

from setuptools.command.test import test


def jogar():
    print("Bem-vindo ao Roda a roda")
    arquivo=open("palavras.txt","r")
    palavras=[]
    for linha in arquivo:
        palavras.append(linha)
    arquivo.close()
    numero = int(random.randrange(0, len(palavras)))
    palavra_escolhida=palavras[numero].strip().upper()

    letras_encotradas= ['_' for letra in palavra_escolhida]
    enforcado=False
    acerto=False
    erros=0
    while(not enforcado and not acerto):
        tentativa=input('Diga uma letra:')
        tentativa=tentativa.strip().upper()

        if(tentativa in palavra_escolhida):
            index=0
            for letra in palavra_escolhida:
                if(tentativa == letra):
                    letras_encotradas[index] = letra
                index+=1
        else:
            erros += 1
            forca(erros)
        enforcado= erros == 7
        acerto="_" not in letras_encotradas

        print(letras_encotradas)

    if(acerto):
        imprime_venceu()
    else:
        imprime_perdeu(palavra_escolhida)

    print('acabou')

def imprime_perdeu(palavra_escolhida):
    print(f"A palavra era {palavra_escolhida}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_venceu():
    print("Parabéns, você venceu!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(erros == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (erros == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()