import random


def jogar():
    print('Bem-vindo ao jogo')

    numero_objetivo = int(random.randrange(1, 101))

    dificuldade=0
    pontosTotal=1000
    pontos=pontosTotal
    while dificuldade==0:
        print('Selecione a dificuldade:\n(1) Fácil\n(2) Médio\n(3) Díficil\n')
        dificuldade=int(input())

        if dificuldade == 1:
            numero_tentativas = 15
        elif dificuldade == 2:
            numero_tentativas = 10
        elif dificuldade == 3:
            numero_tentativas = 5
        else:
            dificuldade = 0
            print("Mas tu é burro mesmo hein!")


    numero_tentativa_atual=numero_tentativas

    while(numero_tentativa_atual>0):
        print(f"Você tem {numero_tentativa_atual} de {numero_tentativas} tentativas")
        chute_string = input("Qual é seu chute? (1-100)")
        chute_integer = int(chute_string)

        if (chute_integer < 1 or chute_integer > 100):
            print('Seu numero é maior que 100 ou menor 1! seu burro!')
        acertou = chute_integer == numero_objetivo
        maior = chute_integer > numero_objetivo
        menor = chute_integer < numero_objetivo

        print(f"Você chutou:{chute_integer}")

        if acertou:
            print('você acertou! parabens')
            break
        else:
            if maior:
                print("O numero é menor")
            elif menor:
                print("O numero é maior")
            pontos-=pontosTotal/numero_tentativas
        numero_tentativa_atual -= 1
    print(f"Fim! sua pontuação final foi: {pontos}")

