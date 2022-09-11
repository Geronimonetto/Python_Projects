from Dados_clientes import cliente_devedor,lista_nova
from functools import reduce

def mensagem_inicial(padrao = 'Sistema de clientes'):
    print("--"*20)
    print(padrao.center(40))
    print("--"*20)

def lista_devedores(total_devedores):
    lista_dev = [(x['cliente'], x['debito']) for x in total_devedores]
    totaldebito = reduce(lambda tot, x: x['debito'] + tot,total_devedores,0)
    print("☆☆"*14)
    print(f"{'Clientes Devedores'}".center(40))
    print('☆☆'*14)
    print()

    for i,v in lista_dev:
        print(f"{i:<10}\033[31m{'R$':>20} {v:.2f}\033[m".replace('.',','))

    print("--"*20)
    print(f"{'Total':<10}\033[31m{'R$':>20} {totaldebito:.2f}\033[m".replace(".",","))
    print()
    return lista_dev
def mensagem_cliente(padrao='clientes devedores'):
     return mensagem_inicial

def excluir_debito(lista_devedores):

        nome = str(input('Nome do cliente: ')).strip().capitalize()
        while len(nome)<1 or nome.isnumeric():
            print("\033[31mPor favor, Digite um cliente válido!\033[m")
            break
        else:
            for i in cliente_devedor:
                for valores in i.values():
                    if valores == nome:
                        cliente_devedor.remove(i)
            print()
            print(f"\033[032mCliente e Débitos Removidos com Sucesso!\33[m")


def adicionar_cliente(lista_clientes):
        lista_nova['cliente'] = input("Nome do cliente: ").strip().capitalize()
        lista_nova['debito'] = float(input("Valor do débito: "))
        cliente_devedor.append(lista_nova.copy())
        lista_nova.clear()
        print()
        print(f"\033[032mDébito Adicionado com Sucesso\033[m")


