from Dados_clientes import cliente_devedor,lista_nova
from Funcoes_clientes import mensagem_inicial,lista_devedores,mensagem_cliente,excluir_debito,adicionar_cliente

while True:

    mensagem_inicial()
    opcao = input("Escolha a Opção \n\t[ 1 ] Lista De Devedores\n"
                  "\t[ 2 ] Excluir Débito\n"
                  "\t[ 3 ] Adicionar Debito:  " )
    print()
    mensagem_cliente()
    if opcao =='1':
        lista_devedores(cliente_devedor)

    elif opcao =='2':
        excluir_debito(cliente_devedor.copy())

    elif opcao =='3':
        adicionar_cliente(lista_nova)


