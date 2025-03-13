import random

def jogar():
    jogador = input("Use Pedra, Papel ou Tesoura: ").lower()
    computador = random.choice(['pedra','papel','tesoura'])
    print (f"O computador escolheu {computador.title()}")

    if jogador == computador:
        return "Empate"

    # p > t, t > pa, pa > p
    if ganhou(jogador, computador):
        return "Você ganhou!"
    
    return 'Você perdeu!'

def ganhou(jogador, computador):
    # return true se o jogador ganhar
    # p > t, t > pa, pa > p
    if (jogador == 'pedra' and computador == 'tesoura') or (jogador == 'tesoura' and computador == 'papel') or (jogador == 'papel' and computador == 'pedra'):
        return True
    
print(jogar())
