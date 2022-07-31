"""

                                                                    Jogo da forca    by: Geronimo Neto


"""
import random
chances = 3
palavra_chave = ["Sport","Vasco","Corinthias","Flamengo","Palmeiras"]
palavra_selecionada = random.choice(palavra_chave).upper()
lista_de_palavras = []
print("-*"*20)
print("--- JOGO DA FORCA ---".center(40))
print("-*"*20)
print("Tente adivinhar qual palavra eu estou pensando ...".center(20))
vazio = ""
print()

while chances <=3:
    palavra_jogador = str(input("Digite uma letra: ")[0].upper())

    for p in palavra_selecionada:

        if p == palavra_jogador:
            print(p,end="")
            lista_de_palavras.append(p)
        else:
            print("*",end="")

