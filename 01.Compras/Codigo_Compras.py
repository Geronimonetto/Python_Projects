"""

                                                                Comprando Frutas    by:Geronimo Neto

"""
import time

print("**"*30)
print("SEJA BEM VINDO AO SHOOPING DAS FRUTAS".center(60))
print("**"*30)
print()

totaldacompra =0
compras = []
produtos = {}

while True:
    item = input("Qual Produto Deseja Comprar\n[ 1 ] Melancia  [ 2 ] Melão  [ 3 ] Abóbora: ")
    peso = input("Quantos KG: ")

    if not item.isnumeric() and not peso.isnumeric():
        print("Por favor digite um número entre 1 a 3!!")
    else:
        item = int(item)
        peso = float(peso)

    if item ==1:
        produtos['Produto'] = "Melancia"
        produtos['KG'] = peso
        produtos['Preço'] = 2.50
        produtos['Valor da compra'] = 2.50*peso
    elif item == 2:
        produtos['Produto'] = "Melão"
        produtos['KG'] = peso
        produtos['Preço'] = 4.00
        produtos['Valor da compra'] = 4.00*peso
    elif item ==3:
        produtos['Produto'] = "Abóbora"
        produtos['KG'] = peso
        produtos['Preço'] = 3.50
        produtos['Valor da compra'] = 3.50 * peso
    else:
        print(f"Não encontramos a opção que você escolheu, Escolha uma produto entre 1 a 3!!")

    compras.append(produtos.copy())

    opcao = input("Finalizar compra [S/N]: ").upper().lstrip()
    while opcao not in "SN" and not opcao.isalpha():
        print("Por favor digite uma opção válida!")
        opcao = input("Finalizar compra [S/N]: ").upper().lstrip()
    if opcao in "Ss":
        print("Salvando suas compras ...")
        break

time.sleep(1)

print()
print("Suas compras foram: ")
print("--"*30)

for n,c in enumerate(compras):
    print(f"Item {n+1}")
    for x,i in c.items():
        print(f"{x:<15}{i:>30}")
        if x == 'Valor da compra':
            totaldacompra += i
    print("--" * 30)
print(f"Total das compras  {'R$':>21}{totaldacompra:.2f}")


