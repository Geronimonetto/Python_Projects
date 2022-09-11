"""
                                                                                    IMC  by:Geronimo Neto

"""

from time import sleep
Nome_pessoa = str(input("Qual o seu nome: "))

idade_pessoa = int(input("Qual a sua idade: "))
Pesoatual = float(input("Por favor digite seu peso atual: "))
Altura_pessoa = float(input("Qual a sua altura: "))

Formulaimc = Pesoatual / (Altura_pessoa**2)

print("Espere um pouco enquanto eu Calculo seu IMC ...")
sleep(3)
if Formulaimc < 18.5:
    print(f"\033[1;31m{Nome_pessoa} Cuidado!! Você está abaixo do peso!")
elif Formulaimc >= 18.5 and Formulaimc <= 24.9:
    print(f"\033[1;32m{Nome_pessoa} Perfeito!! Você está com o seu peso normal\033[32m!")
elif Formulaimc >= 25.0 and Formulaimc <= 29.9:
    print(f"\033[1;33m{Nome_pessoa} Alerta!! Tome cuidado você está com sobrepreso.")
elif Formulaimc >= 30.0 and Formulaimc <=34.9:
    print(f"\033[1;31m{Nome_pessoa} é Indicado procurar um nutricionista ou prática de "
    f"atividade física, Você está com Obesidade Grau 1.")
elif Formulaimc >= 35 and Formulaimc <=39.9:
    print(f"\033[1;31m{Nome_pessoa} Você precisa procurar um médico,Você está com Obesidade Grau 2\n"
    f"e pode desenvolver várias doenças crônicas entre elas estão:\n1.Hipertensão\n2.Diabetes\n"
    f"3.Seu índice de colesterol está alto\n4.Hipertrofia Ventricular\n5.Doenças Respitarórias.")
elif Formulaimc >40:
    print(f"\033[1;31m{Nome_pessoa} Você ultrapassou o limite de Obesidade, Você está com Obesidade Grau 3\n"
    f"e pode desenvolver várias doenças crônicas entre elas estão:\n1.Hipertensão\n2.Diabetes\n"
    f"3.Seu índice de colesterol está alto\n4.Hipertrofia Ventricular\n5.Doenças Respitarórias.")