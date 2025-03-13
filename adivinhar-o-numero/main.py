import random

def adivinhar(x):
    numero_random = random.randint(1, x)
    chute = 0
    while chute != numero_random:
        chute = int(input(f"Adivinhe um numero entre 1 e {x}: "))
        if chute < numero_random:
            print("Você errou, tente novamente. (O numero estava abaixo.)")
        elif chute > numero_random:
            print("Você errou, tente novamente. (O numero estava acima.)")

    print(f"Voce acertou o numero {numero_random} corretamente!")

def computador_adivinhar(x):
    menor = 1
    maior = x
    feedback = ""
    while feedback != "c":
        if menor != maior:
            chute = random.randint(menor, maior)
        else:
            chute = menor #poderia ser maior menor = maior
        feedback = input(f"O {chute} esta acima (A), abaixo (AB), ou correto (C)?").lower()
        if feedback == 'a':
            maior = chute - 1
        elif feedback == "ab":
            menor = chute + 1

    print(f"O computador acertou o seu numero, {chute} corretamente!")
    



computador_adivinhar(10)
