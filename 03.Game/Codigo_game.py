import random
times = ["Sport","Palmeiras","Flamengo","Corinthians","Cruzeiro"]
times_vazio = []
sorteio = random.choice(times).upper()
print("*-*"*20)
print("BEM VINDO AO JOGO DA FORCA".center(60))
print("*-*"*20)
chances = 3
while True:
    letra = input("Escreva uma letra: ").strip().upper()
    if not letra.isalpha():
        print("Usuário digite apenas letras!!")
        continue
    if len(letra) > 1:
        print("Digite apenas 1 letra por vez!!")
        continue

    times_vazio.append(letra)

    if letra in sorteio:
        print("Você acertou!! Tem essa letra na palavra")
    else:
        print("Você errou!! Infelizmente não tem essa letra na palavra\nTente novamente!!")

    palavra_completa = ""
    for letra_nova in sorteio:
        if letra_nova in times_vazio:
            palavra_completa += letra_nova
        else:
            palavra_completa += "_"
    if palavra_completa == sorteio:
        print(f"Parabéns, A palavra secreta era {palavra_completa}")
        break
    else:
        print(f"A palavra ainda está assim : {palavra_completa}")
    if letra not in sorteio:
        chances -= 1
        if chances ==0:
            print("infelizmente acabaram suas chances.")
            break
    print(f"Você ainda tem {chances} chances!")
