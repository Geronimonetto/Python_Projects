"""

                                                                PAROUIMPAR     by:Geronimo Neto


"""
import time 
print("-"*30)
print("PROGRAMA PAR OU IMPAR".center(30))
print("-"*30)
numero = input("Digite um número: ")

if numero.isdigit():
    numero = int(numero)
    print("Verificando aguarde...")
    time.sleep(1)
    if numero % 2 ==0:
        print(f"O número {numero} é PAR!")
    else:
        print(f"O número {numero} é IMPAR!")
else:
    print("Por favor digite um número válido!")    
